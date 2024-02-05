from urllib import request
from django.http import HttpResponse
from rest_framework import serializers, viewsets
from .models import CareerProfessional
from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import SignupForm





def scholarships(request):
    return render(request, 'polls/scholarships.html')

def chatai(request):
    return render(request, 'polls/chatgpt.html')

def redirect_to_remote_url(request):
    remote_url = "https://shahshaurya8.wixsite.com/my-site-2"  # Replace this with your remote URL
    return redirect(remote_url)

