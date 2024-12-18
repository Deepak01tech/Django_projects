from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('create/', views.create_user, name='create_user'),
    path('update/<int:id>/', views.update_user, name='update_user'),
    path('delete/<int:id>/', views.delete_user, name='delete_user'),
    path('profile/<int:id>/', views.manage_profile, name='manage_profile'),
]
