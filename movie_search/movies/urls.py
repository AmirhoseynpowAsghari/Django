from django.urls import path
from .views import movie_search_view

urlpatterns = [
    path('search/', movie_search_view, name='movie-search'),
]