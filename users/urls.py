from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_view, name='Login'),
    # path('register/', views.register_view, name='Register'),
    path('dashboard/', views.dashboard_view, name='Dashboard'),
    # Profile
    path('profile/', views.userProfileView, name="Profile"),
    path('profile/view/', views.userProfileEdit, name="Profile View"),
    path('profile/update', views.userProfileUpdate, name="Profile Update"),
    path('profile/update/location', views.userProfileLocation, name="Profile location Update"),
    path('users/locations/map', views.usersLocationMap, name="Locations"),

    path('register/', views.userSignup, name="Register"),
    path('logout/', views.logoutUser, name="Logout")
]