from django.urls import path
from . import views


urlpatterns = [
    path('reviews/', views.ReviewListCreateView.as_view(), name='review-create-list-view'),
    path('reviews/<int:pk>/', views.ReviewRetriveUpdateDestroyView.as_view(), name='review-detail-view'),
]
