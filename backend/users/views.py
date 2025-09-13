from django.shortcuts import render
from rest_framework import authentication, generics, permissions
from .models import User
from .serializers import UserSerializer
# from .permissions import IsAdmin,IsCashier,IsManager
# Create your views here.
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset =  User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]
class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes= [permissions.DjangoModelPermissions]
    lookup_field = 'username'