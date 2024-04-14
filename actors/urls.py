from django.urls import path
from . import views

urlpatterns = [
    path('actors/', views.ActorListCreateView.as_view(), name='actor-create-list-view'),
    path('actors/<int:pk>/', views.ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-view'),
]
