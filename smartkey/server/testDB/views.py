from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import test_db
from .serializers import TestSerializer
import json, datetime, logging, time

logger = logging.getLogger(__name__)

class TestDB(APIView):
    # Post
    def post(self, request):
        # body에서 정보를 뽑아와서 object를 save할 예정
        data = JSONParser().parse(request)
        test_serializer = TestSerializer(data = data)

        if test_serializer.is_valid():
            test_serializer.save()
            return HttpResponse(test_serializer.data, status = status.HTTP_200_OK)
        else:
            return HttpResponse(test_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    # Get
    # Get /pk
    def get(self, request, **kwargs):
        test_serializer = None
        if kwargs.get('pk') is None:
            q = test_db.objects.all()
            test_serializer = test_serializer(q, many = True)
        else:
            pk = kwargs.get('pk')
            q = test_db.objects.get(id = pk)
            test_serializer = test_serializer(q)

        if test_serializer.is_valid():
            test_serializer.save()
            return HttpResponse(test_serializer.data, status = status.HTTP_200_OK)
        else:
            return HttpResponse(test_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    
    '''
    # Put
    def put(self, request, **kwargs):
        

        response = HttpResponse(ret, status = status.HTTP_200_OK)

        return response

    # Delete
    def delete(self, request, **kwargs):
        ret = ""

        response = HttpResponse(ret, status = status.HTTP_200_OK)

        return response
    '''