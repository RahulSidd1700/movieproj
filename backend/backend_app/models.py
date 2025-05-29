from django.db import models

class Usertable(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Movietable(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    genre = models.CharField(max_length=100)
    rating = models.IntegerField()
    review = models.TextField()
    watched_date = models.DateField(null=True, blank=True)
    image_url = models.URLField(blank=True, null=True)  # <-- Added this line
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class MovieUser(models.Model):
    movie = models.ForeignKey(Movietable, on_delete=models.CASCADE, related_name='users')
    user = models.ForeignKey(Usertable, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"



