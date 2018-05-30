from django.db import models
from django.utils import timezone

class Genre(models.Model):
    genre = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.genre

class Book(models.Model):
    author = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200, default="/static/bliss-images/")
    year = models.IntegerField()
    text = models.TextField()
    pdf = models.CharField(max_length=200, default="/static/bliss-files/")
    bestseller = models.IntegerField(default=0)

    def __str__(self):
            return self.title

class Blog(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

class CommentBook(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)