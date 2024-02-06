from urllib import request
from .models import CareerProfessional
from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import *





def scholarships(request):
    return render(request, 'polls/scholarships.html')

# def chatai(request):
#     return render(request, 'polls/chatgpt.html')

def redirect_to_remote_url(request):
    remote_url = "https://shahshaurya8.wixsite.com/my-site-2"  # Replace this with your remote URL
    return redirect(remote_url)

def resedu(request):
    model = Scholarship.objects.all()
    context = {
        'scholarships':model
    }
    print(f"context is {context}")
    return render(request, 'polls/resedu.html', context)

def eventedu(request):
    return render(request, 'polls/eventedu.html')

def edtech(request):
    return render(request, 'polls/edtech.html')

def adhyaana(request):
    return render(request, 'polls/adhyaana_ai.html')   

def dhyaana(request):
    return render(request, 'polls/dhyaana_ai.html')

def healthtech(request):
    return render(request, 'polls/healthtech.html')