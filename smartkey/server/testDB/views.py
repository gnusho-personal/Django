from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
import json, datetime, logging, time

logger = logging.getLogger(__name__)

class TestDB(APIView):
    # Post
    def post(self, request):
        
        a = request.GET.get('a', -1)
        response = HttpResponse('Hello World Post', status = status.HTTP_200_OK)
        time.sleep(10)

        return response

    # Get
    def get(self, request, **kwargs):

        ret = 'Hello World Get'
        if kwargs.get('pk') is not None:
            pk = kwargs.get('pk')
            ret += ' ' + str(pk)
        
        a = request.GET.get('a', -1)
        ret += ' ' + str(a)
        
        response = HttpResponse(ret, status = status.HTTP_200_OK)
        time.sleep(100)

        return response

    # Put
    def put(self, request, **kwargs):

        ret = 'Hello World Put'
        if kwargs.get('pk') is not None:
            pk = kwargs.get('pk')
            ret += ' ' + str(pk)

        a = request.GET.get('a', -1)
        ret += ' ' + str(a)

        response = HttpResponse(ret, status = status.HTTP_200_OK)

        return response

    # Delete
    def delete(self, request, **kwargs):

        ret = 'Hello World Del'
        if kwargs.get('pk') is not None:
            pk = kwargs.get('pk')
            ret += ' ' + str(pk)
        
        a = request.GET.get('a', -1)
        ret += ' ' + str(a)

        response = HttpResponse(ret, status = status.HTTP_200_OK)

        return response