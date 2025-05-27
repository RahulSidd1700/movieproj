from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse,HttpResponse
from .models import Movietable,Usertable

@api_view(['GET','POST'])
def users(request):
    if(request.method=='GET'):
        users=list(Usertable.objects.all().values())
        return JsonResponse(users,safe=False)
    elif(request.method=='POST'):
        data=request.data 
        user=Usertable(username=data["username"],
        password=data["password"],
        email=data["email"])
        user.save()
        return HttpResponse("Successfully created")

@api_view(['PUT',"DELETE"])    
def user_change(request,user_id):
    user=Usertable.objects.get(id=user_id)
    if(request.method=="PUT"):
        data=request.data 
        user.username=data.get("username",user.username)
        user.password=data.get("password",user.password)
        user.email=data.get("email",user.email)
        user.save()
        return HttpResponse("Updated")
    elif(request.method=='DELETE'):
        user.delete()
        return HttpResponse("Deleted")




# @api_view(['POST'])
# def register_user(request):
    
#     return JsonResponse({"message": "User registered successfully."})

# @api_view(['POST'])
# def login_user(request):
    
#     return JsonResponse({"message": "User logged in successfully."})

# @api_view(['POST'])
# def logout_user(request):
    
#     return JsonResponse({"message": "User logged out successfully."})


@api_view(['GET', 'POST'])
def get_movies(request, user_id):
    user = Usertable.objects.get(id=user_id)

    if request.method == 'GET':
        movies = Movietable.objects.filter(user=user).values()
        return JsonResponse({"movies": list(movies)}, safe=False)

    if request.method == 'POST':
        data = request.data

        if 'title' not in data or data['title'] == "":
            return JsonResponse({"error": "Title is required"}, status=400)

        if 'year' not in data or data['year'] == "":
            return JsonResponse({"error": "Year is required"}, status=400)

        if 'genre' not in data or data['genre'] == "":
            return JsonResponse({"error": "Genre is required"}, status=400)

        if 'rating' not in data or data['rating'] == "":
            return JsonResponse({"error": "Rating is required"}, status=400)

        if 'review' not in data or data['review'] == "":
            return JsonResponse({"error": "Review is required"}, status=400)

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
    movie = Movietable.objects.get(id=movie_id)  # Will raise error if not found

    if request.method == 'GET':
        return JsonResponse({
            "movie_id": movie.id,
            "title": movie.title,
            "year": movie.year,
            "genre": movie.genre,
            "rating": movie.rating,
            "review": movie.review,
            "watched_date": movie.watched_date,
        })

    elif request.method == 'PUT':
        data = request.data
        movie.title = data.get('title', movie.title)
        movie.year = data.get('year', movie.year)
        movie.genre = data.get('genre', movie.genre)
        movie.rating = data.get('rating', movie.rating)
        movie.review = data.get('review', movie.review)
        movie.watched_date = data.get('watched_date', movie.watched_date)
        movie.save()

        return JsonResponse({"message": "Movie updated successfully"})

    elif request.method == 'DELETE':
        movie.delete()
        return JsonResponse({"message": "Movie deleted successfully"})




