from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def get_all(request):
    obj = Todo.objects.all()
    serializerdata = TodoSerializer(obj , many = True)
    return Response(serializerdata.data)