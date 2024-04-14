from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from app.permissions import GlobalDefaultPermissions
from reviews.models import Review
from reviews.serializers import RevierSerializers


class ReviewListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Review.objects.all()
    serializer_class = RevierSerializers


class ReviewRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Review.objects.all()
    serializer_class = RevierSerializers
