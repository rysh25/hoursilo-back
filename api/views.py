from rest_framework import generics

from api import serializers


class CreateUserView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
