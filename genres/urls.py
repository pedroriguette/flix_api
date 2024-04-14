from django.urls import path
from . import views


urlpatterns = [
    path('genres/', views.GenreListCreateView.as_view(), name='genre-create-list-view'),
    path('genres/<int:pk>/', views.GenreRetrieveUpdateDestroyView.as_view(), name='genres-detail-views'),
]
