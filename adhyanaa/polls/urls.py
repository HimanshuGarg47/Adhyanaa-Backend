from django.urls import path

from . import views

urlpatterns = [
    path('', views.redirect_to_remote_url, name="home"),
    path("scholarships/", views.scholarships, name="scholarships"),
    path("chatai/", views.chatai, name="chatai") 

]