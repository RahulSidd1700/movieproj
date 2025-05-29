from django.contrib import admin
from django.urls import path
from backend_app import views

urlpatterns = [
    path("users/", views.users),
    path("users/<int:user_id>/", views.user_change),
    path("api/movies/user/<int:user_id>/", views.get_movies),
    path("api/movies/<int:movie_id>/", views.get_movie_details),
    path("api/movies/all/", views.get_all_movies),
    path("api/wishlist/<int:user_id>/", views.get_user_movies),
    path("api/wishlist/<int:user_id>/<int:movie_id>/", views.add_movie_to_wishlist),
    
]
