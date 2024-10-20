from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create a new client
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_client(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by=request.user)  # Set created_by to the current user
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# List all clients
@api_view(['GET'])
@permission_classes([AllowAny])  # Allow anyone to view the clients
def list_clients(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)

# Retrieve client and associated projects
@api_view(['GET'])
def get_client(request, pk):
    try:
        client = Client.objects.get(pk=pk)
        projects = Project.objects.filter(client=client)  # Get all projects related to this client
        project_data = ProjectSerializer(projects, many=True).data  # Serialize the project data

        client_data = ClientSerializer(client).data  # Serialize the client data
        client_data['projects'] = project_data  # Add the project data to the client response

        return Response(client_data)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


# Update client
@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])  # Optional: If you want to require authentication
def update_client(request, pk):
    try:
        client = Client.objects.get(pk=pk)
        serializer = ClientSerializer(client, data=request.data, partial=True)  # Enable partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


# Delete client
@api_view(['DELETE'])
def delete_client(request, pk):
    try:
        client = Client.objects.get(pk=pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_project(request, client_id):
    try:
        # Get the client by client_id from the URL
        client = Client.objects.get(id=client_id)

        # Retrieve project name from request data
        project_name = request.data.get('project_name')

        # Extract user IDs from the request
        users_data = request.data.get('users')
        users_ids = [user['id'] for user in users_data]

        # Create a new project and associate it with the client
        project = Project.objects.create(
            project_name=project_name,
            client=client,
            created_by=request.user  # Assuming the logged-in user is the creator
        )

        # Assign the already registered users to the project
        project.users.set(User.objects.filter(id__in=users_ids))
        project.save()

        # Prepare the response data
        response_data = {
            'id': project.id,
            'project_name': project.project_name,
            'client': client.client_name,
            'users': [{'id': user.id, 'name': user.username} for user in project.users.all()],
            'created_at': project.created_at,
            'created_by': request.user.username  # Assuming the logged-in user is the creator
        }

        return Response(response_data, status=status.HTTP_201_CREATED)
    except Client.DoesNotExist:
        return Response({'error': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# List all projects assigned to the logged-in user

@api_view(['GET'])
def list_user_projects(request):
    try:
        # Get all projects where the logged-in user is assigned
        user_projects = Project.objects.filter(users=request.user)

        # Serialize the projects
        project_data = [
            {
                'id': project.id,
                'project_name': project.project_name,
                'created_at': project.created_at,
                'created_by': project.created_by.username  # Assuming created_by is a User model
            }
            for project in user_projects
        ]

        return Response(project_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

