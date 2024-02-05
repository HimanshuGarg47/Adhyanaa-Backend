from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    # path("index1/", views.index1, name="index1"),
    # path("index2/", views.index2, name="index2"),
    path("scholarships/", views.scholarships, name="scholarships"),
    path("chatai/", views.chatai, name="chatai") 

]