
from django.contrib import admin
from django.urls import path
from backend_app import views

urlpatterns = [
    # path("api/auth/register/", views.register_user),
    # path("api/auth/login/", views.login_user),
    # path("api/auth/logout/", views.logout_user),
    path("users/",views.users),
    path("users/<int:user_id>/",views.user_change),
    path("api/movies/user/<int:user_id>/", views.get_movies),
    path("api/movies/<int:movie_id>/", views.get_movie_details)
]

