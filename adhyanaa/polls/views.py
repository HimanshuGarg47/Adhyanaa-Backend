from urllib import request
from django.http import HttpResponse
from rest_framework import serializers, viewsets
from .models import CareerProfessional
from django.shortcuts import render
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

@login_required
def login(request):
    return render(request, 'polls/login3.html')
 
 def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('index1')
#     else:
#         form = UserCreationForm()
#     return render(request, 'polls/signup.html', {'form': form})



def scholarships(request):
    return render(request, 'polls/scholarships.html')

def chatai(request):
    return render(request, 'polls/chatgpt.html')







# class CareerProfessionalViewSet(viewsets.ModelViewSet):
#     queryset = CareerProfessional.objects.all()
#     serializer_class = CareerProfessionalSerializer

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")