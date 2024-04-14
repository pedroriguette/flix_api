from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from app.permissions import GlobalDefaultPermissions
from actors.serializers import ActorsSerializers
from actors.models import Actors


class ActorListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializers


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializers
