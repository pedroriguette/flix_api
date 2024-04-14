from django.urls import path
from movies.views import MovieStatsView
from . import views

urlpatterns = [
    path('movies/', views.MovieListCreateView.as_view(), name='movie-create-list-view'),
    path('movies/<int:pk>/', views.MovieRetriveUpdateDestroyView.as_view()),
    path('movies/stats/', MovieStatsView.as_view(), name='movie-stats-view'),
]
