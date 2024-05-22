from django.urls import path
from .views import fetch_movies


urlpatterns = [
    path('/', fetch_movies, name="Fetch movies"),
]
