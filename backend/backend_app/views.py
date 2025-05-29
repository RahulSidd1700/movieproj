from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
from .models import Movietable, Usertable,MovieUser

@api_view(['GET', 'POST'])
def users(request):
    if request.method == 'GET':
        users = list(Usertable.objects.all().values())
        return JsonResponse(users, safe=False)
    elif request.method == 'POST':
        data = request.data
        user = Usertable(
            username=data["username"],
            password=data["password"],
            email=data["email"]
        )
        user.save()
        return HttpResponse("Successfully created")

@api_view(['PUT', 'DELETE'])    
def user_change(request, user_id):
    user = Usertable.objects.get(id=user_id)
    if request.method == "PUT":
        data = request.data
        user.username = data.get("username", user.username)
        user.password = data.get("password", user.password)
        user.email = data.get("email", user.email)
        user.save()
        return HttpResponse("Updated")
    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse("Deleted")

@api_view(['GET', 'POST'])
def get_movies(request, user_id):
    user = get_object_or_404(Usertable, id=user_id)
    if request.method == 'GET':
        movies = Movietable.objects.filter(user=user).values()
        return JsonResponse({"movies": list(movies)}, safe=False)
    if request.method == 'POST':
        data = request.data
        required_fields = ['title', 'year', 'genre', 'rating', 'review']
        for field in required_fields:
            if not data.get(field):
                return JsonResponse({"error": f"{field.capitalize()} is required"}, status=400)
        movie = Movietable.objects.create(
            title=data['title'],
            year=data['year'],
            genre=data['genre'],
            rating=data['rating'],
            review=data['review'],
            watched_date=data.get('watched_date'),
            user=user
        )
        return JsonResponse({
            "message": "Movie added successfully",
            "movie_id": movie.id
        }, status=201)

@api_view(['GET', 'PUT', 'DELETE'])
def get_movie_details(request, movie_id):
    movie = Movietable.objects.get(id=movie_id)
    if request.method == 'GET':
        return JsonResponse({
            "movie_id": movie.id,
            "title": movie.title,
            "year": movie.year,
            "genre": movie.genre,
            "rating": movie.rating,
            "review": movie.review,
            "watched_date": movie.watched_date,
            "image_url": movie.image_url,
        })
    elif request.method == 'PUT':
        data = request.data
        for field in ['title', 'year', 'genre', 'rating', 'review', 'watched_date']:
            setattr(movie, field, data.get(field, getattr(movie, field)))
        movie.save()
        return JsonResponse({"message": "Movie updated successfully"})
    elif request.method == 'DELETE':
        movie.delete()
        return JsonResponse({"message": "Movie deleted successfully"})

@api_view(['GET'])
def get_all_movies(request):
    movies = Movietable.objects.all().values()
    return JsonResponse({"movies": list(movies)}, safe=False)

@api_view(["GET"])
def get_user_movies(request, user_id):
    try:
        user = Usertable.objects.get(id=user_id)
        movies = MovieUser.objects.filter(user=user)
        movie_list = []
        for movie_user in movies:
            movie = movie_user.movie
            movie_list.append({
                "movie_id": movie.id,
                "title": movie.title,
                "year": movie.year,
                "genre": movie.genre,
                "rating": movie.rating,
                "review": movie.review,
                "watched_date": movie.watched_date,
                "image_url": movie.image_url
            })
        return JsonResponse({"movies": movie_list}, safe=False)
    except Usertable.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)
    except Movietable.DoesNotExist:
        return JsonResponse({"error": "Movie not found for this user"}, status=404)

@api_view(['POST','DELETE'])
def add_movie_to_wishlist(request, user_id, movie_id):
    if(request.method == 'POST'):
        try:
            user = Usertable.objects.get(id=user_id)
            movie = Movietable.objects.get(id=movie_id)
            if MovieUser.objects.filter(user=user, movie=movie).exists():
                return JsonResponse({"message": "Movie already in wishlist"}, status=400)
            else:
                MovieUser.objects.create(user=user, movie=movie)
                return JsonResponse({"message": "Movie added to wishlist successfully"}, status=201)
        except Usertable.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)
        except Movietable.DoesNotExist:
            return JsonResponse({"error": "Movie not found"}, status=404)
    elif request.method == 'DELETE':
        try:
            user = Usertable.objects.get(id=user_id)
            movie = Movietable.objects.get(id=movie_id)
            movie_user = MovieUser.objects.get(user=user, movie=movie)
            if not movie_user:
                return JsonResponse({"error": "Movie not found in user's wishlist"}, status=404)
            movie_user.delete()
            return JsonResponse({"message": "Movie removed from wishlist successfully"}, status=200)
        except MovieUser.DoesNotExist:
            return JsonResponse({"error": "Movie not found in user's wishlist"}, status=404)
        except Usertable.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)
        except Movietable.DoesNotExist:
            return JsonResponse({"error": "Movie not found"}, status=404)