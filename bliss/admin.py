from django.contrib import admin
from .models import Book
from .models import Blog
from .models import Genre
from .models import Comment
from .models import CommentBook

admin.site.register(Book)
admin.site.register(Blog)
admin.site.register(Genre)
admin.site.register(Comment)
admin.site.register(CommentBook)