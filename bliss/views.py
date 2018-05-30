from django.shortcuts import render_to_response, redirect, render, get_object_or_404
from django.utils import timezone
from .models import Book, Genre, Blog, Comment, CommentBook
from .forms import BlogForm, CommentForm
from .forms import UserEditForm, CommentFormBook
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.template.context_processors import csrf
from django.contrib import auth

genres = Genre.objects.all()
def index(request):
	books = Book.objects.all()
	return render(request, 'bliss/index.html', {'books':books, 'genres':genres})

def contacts(request):
	return render(request, 'bliss/contacts.html', {'genres':genres})

def blog(request):
	blogs = Blog.objects.all()
	return render(request, 'bliss/blog.html', {'genres':genres, 'blogs':blogs}) 

def blognew(request):
	if request.method == "POST":
		form = BlogForm(request.POST)
		if form.is_valid():
			blog = form.save(commit=False)
			blog.author = request.user
			blog.created_date = timezone.now()
			blog.save()
			return redirect('blogdetail', pk=blog.pk)
	else:
		form = BlogForm()
		return render(request, 'bliss/blog_new.html', {'form': form})

def blogedit(request, pk):
	blog = get_object_or_404(Blog, pk=pk)
	if request.method == "POST":
		form = BlogForm(request.POST, instance=blog)
		if form.is_valid():
			blog = form.save(commit=False)
			blog.author = request.user
			blog.created_date = timezone.now()
			blog.save()
			return redirect('blogdetail', pk=blog.pk)
	else:
		form = BlogForm(instance=blog)
		return render(request, 'bliss/blog_new.html', {'form': form})

def blogdetail(request, pk):
	blog = get_object_or_404(Blog, pk=pk)
	blogcomment = Comment.objects.filter(blog=blog)
	return render(request, 'bliss/blog_detail.html', {'blog': blog, 'blogcomment': blogcomment} )

def genredetail(request, pk):
	genre = get_object_or_404(Genre, pk=pk)
	booksgenre = Book.objects.filter(genre=genre)
	return render(request, 'bliss/genre_detail.html', {'genre': genre, 'booksgenre': booksgenre})

def bookdetail(request, pk):
	book = get_object_or_404(Book, pk=pk)
	commentbook = CommentBook.objects.filter(book=book)
	return render(request, 'bliss/book_detail.html', {'book': book, 'commentbook': commentbook})

def user(request, pk):
	user = get_object_or_404(User, pk=pk)
	return render(request, 'bliss/blog_detail.html', {'user': user})

def comment(request, pk):
	blog = get_object_or_404(Blog, pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.author = request.user
			comment.created_date = timezone.now()
			comment.blog = blog
			comment.save()
			return redirect('blogdetail', pk=pk)
	else:
		form = CommentForm()
		return render(request, 'bliss/comment.html', {'form': form})

def commentbook(request, pk):
	book = get_object_or_404(Book, pk=pk)
	if request.method == "POST":
		form = CommentFormBook(request.POST)
		if form.is_valid():
			commentbook = form.save(commit=False)
			commentbook.author = request.user
			commentbook.created_date = timezone.now()
			commentbook.book = book
			commentbook.save()
			return redirect('bookdetail', pk=pk)
	else:
		form = CommentForm()
		return render(request, 'bliss/commentbook.html', {'form': form})

def register(request):
	args = {}
	args.update(csrf(request))
	args['form'] = UserCreationForm()
	if request.POST:
		newuser_form = UserCreationForm(request.POST)
		if newuser_form.is_valid():
			newuser_form.save()
			newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
			auth.login(request, newuser)
			return redirect('index')
		else:
			args['form'] = newuser_form
	return render_to_response('bliss/register.html', args)

def login(request):
	args = {}
	args.update(csrf(request))
	if request.POST:
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('user')
		else:
			args['login-error'] = "No such user"
			return render_to_response('bliss/login.html', args)
	else:
		return render_to_response('bliss/login.html', args)

def logout(request):
	auth.logout(request)
	return redirect('/bliss/')

def user(request):
	return render(request, 'bliss/user.html')

def edit(request):
	if request.method == "POST":
		form = UserEditForm(request.POST, instance=request.user)
		if form.is_valid:
			form.save()
			return redirect('user')
	else:
		form = UserEditForm(instance=request.user)
		return render(request, 'bliss/edit.html', {'form': form})

def bloguser(request):
	blogs = Blog.objects.filter(author=request.user)
	return render(request, 'bliss/bloguser.html', {'blogs': blogs})

def deleteBlog(request, pk):
	blog = get_object_or_404(Blog, pk=pk)
	blog.delete()
	return redirect('bloguser')

def deleteUser(request):
	request.user.delete()
	return redirect('index')