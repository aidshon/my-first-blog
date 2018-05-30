from django import forms
from .models import Blog
from .models import Comment
from .models import CommentBook
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ('title', 'text')

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('text',)

class CommentFormBook(forms.ModelForm):
	class Meta:
		model = CommentBook
		fields = ('text',)

class UserEditForm(UserChangeForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'password')