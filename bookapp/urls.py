from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path("today/", views.hijri_today, name="today"),
    path("month/", views.hijri_month, name="month"),
]