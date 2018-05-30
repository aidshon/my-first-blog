from django.shortcuts import render

def index(request):
	return render(request, 'example/home.html') # выводить огромные блоки кода 
# Create your views here.
	