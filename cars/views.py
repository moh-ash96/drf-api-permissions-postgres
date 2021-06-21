from rest_framework import generics
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Car
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer


class CarList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Car.objects.all()
    serializer_class = PostSerializer

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Car.objects.all()
    serializer_class = PostSerializer
