from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.

# so basically the crud operations performed by the function based views can be replaced with the class based view by using the viewsets.modelviewset
# the viewsets.modelviewset is a class based view that provides the crud operations


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
