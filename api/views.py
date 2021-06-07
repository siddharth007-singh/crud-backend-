from django.shortcuts import render
from .models import *
from .serializer  import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def create(r):
    ser = StudentSerializer(data = r.data)
    if ser.is_valid():
        ser.save()
    return Response(ser.data)


@api_view(['GET'])
def show(r):
    event = Student.objects.all()
    ser = StudentSerializer(event, many=True)
    return Response(ser.data)


@api_view(['GET'])
def showfilter(r, pk):
    event = Student.objects.get(id = pk)
    ser = StudentSerializer(event, many=False)
    return Response(ser.data)



@api_view(['DELETE'])
def delete(r, pk):
    event = Student.objects.get(id = pk)
    event.delete()
    return Response('Deleted')




@api_view(['POST'])
def update(r, pk):
    event = Student.objects.get(id = pk)
    ser = StudentSerializer(event, data = r.data)
    if ser.is_valid():
        ser.save()
    return Response(ser.data)