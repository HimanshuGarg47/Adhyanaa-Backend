from django.urls import path

from . import views

urlpatterns = [
    path('', views.redirect_to_remote_url, name="home"),
    path("scholarships/", views.scholarships, name="scholarships"),
    path("resedu/", views.resedu, name="resedu"),
    path("eventedu/", views.eventedu, name="eventedu"),
    path("edtech/", views.edtech, name="edtech"),
    path("adhyaana/", views.adhyaana, name="adhyaana"),
    path("dhyaana/", views.dhyaana, name="dhyaana"),
    path("healthtech/", views.healthtech, name="healthtech"),


]