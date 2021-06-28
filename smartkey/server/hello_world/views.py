from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

class Hello_World(APIView):
    #Post
    def post(self, request):
        return Response('Hello World', status = status.HTTP_200_OK)

    #Get
    def get(self, request, **kwargs):
        return Response('Hello World', status = status.HTTP_200_OK)

    #Put
    def put(self, request, **kwargs):
        return Response('Hello World', status = status.HTTP_200_OK)

    #Delete
    def delete(self, request, **kwargs):
        return Response('Hello World', status = status.HTTP_200_OK)
