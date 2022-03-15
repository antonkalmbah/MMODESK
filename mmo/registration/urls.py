from django.urls import path

from . import views

urlpatterns = [
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('<int:pk>/edit', views.ProfileUpdateView.as_view(), name='edit'),
]