from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def hello_world(request):
    #return HttpResponse("Hello, World!")
    title = "Hello World"
    return render(request, 'signup.html',{
        'form': UserCreationForm,
    })