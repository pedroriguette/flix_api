from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from app.permissions import GlobalDefaultPermissions
from genres.serializers import GenreSerializers
from genres.models import Genre


class GenreListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers
