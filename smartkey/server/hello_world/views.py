from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

class Hello_World(APIView):
    #Post
    def post(self, request):
        return Response('Hello World Post', status = status.HTTP_200_OK)

    #Get
    def get(self, request, **kwargs):
        ret = 'Hello World Get'
        if kwargs.get('pk') is not None:
            pk = kwargs.get('pk')
            ret += ' ' + str(pk)
        return Response(ret, status = status.HTTP_200_OK)

    #Put
    def put(self, request, **kwargs):
        ret = 'Hello World Put'
        if kwargs.get('pk') is not None:
            pk = kwargs.get('pk')
            ret += ' ' + str(pk)
        return Response(ret, status = status.HTTP_200_OK)

    #Delete
    def delete(self, request, **kwargs):
        ret = 'Hello World Del'
        if kwargs.get('pk') is not None:
            pk = kwargs.get('pk')
            ret += ' ' + str(pk)
        return Response(ret, status = status.HTTP_200_OK)
