from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .Serializers import UserSerializer

def index(request):
    return render(request,'medical_api/index.html')

# Create your views here.
class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer