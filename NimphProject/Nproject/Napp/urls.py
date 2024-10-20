from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.create_client, name='create_client'),
    path('clients/list/', views.list_clients, name='list_clients'),
    path('clients/<int:pk>/', views.get_client, name='get_client'),
    path('clients/<int:pk>/update/', views.update_client, name='update_client'),
    path('clients/<int:pk>/delete/', views.delete_client, name='delete_client'),
    path('clients/<int:client_id>/projects/', views.create_project, name='create_project'),
    path('projects/', views.list_user_projects, name='list_user_projects'),
]


# from django.urls import path
# from . import views
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# urlpatterns = [
#     path('clients/', views.list_clients, name='list_clients'),
#     path('clients/', views.create_client, name='create_client'),
#     path('clients/<int:pk>/', views.get_client, name='get_client'),
#     path('clients/<int:pk>/', views.update_client, name='update_client'),
#     path('clients/<int:pk>/', views.delete_client, name='delete_client'),
#     path('clients/<int:client_id>/projects/', views.create_project, name='create_project'),
#     path('projects/', views.list_user_projects, name='list_user_projects'),
#     path('Napp/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('Napp/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]