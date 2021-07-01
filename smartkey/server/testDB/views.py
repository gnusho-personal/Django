from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.viewsets import ModelViewSet
from .models import test_db
from .serializers import TestSerializer
import json, datetime, time

class TestViewSet(ModelViewSet):
    queryset = test_db.objects.all()
    serializer_class = TestSerializer   

    test_list = TestViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })

    test_detail = TestViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    })

'''
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
        if kwargs.get('pk') is None:
            q = test_db.objects.all()
            test_serializer = TestSerializer(data = q, many = True)
            if test_serializer.is_valid():
                test_serializer.save()
                return HttpResponse(test_serializer.data, status = status.HTTP_200_OK)
            else:
                return HttpResponse(test_serializer.errors, status = status.HTTP_400_BAD_REQUEST)    
        else:
            pk = kwargs.get('pk')
            q = test_db.objects.get(id = pk)
            print("\n\n\n\n")
            print(q)
            print("\n\n\n\n")
            test_serializer = TestSerializer(data = q)

            if test_serializer.is_valid():
                test_serializer.save()
                return HttpResponse(test_serializer.data, status = status.HTTP_200_OK)
            else:
                return HttpResponse(test_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    # Put
    def put(self, request, **kwargs):
        

        response = HttpResponse(ret, status = status.HTTP_200_OK)

        return response

    def delete(self, request, **kwargs):
        if kwargs.get('pk') is None:
            return HttpResponse("invalid request", status = status.HTTP_400_BAD_REQUEST)

        else:
            pk = kwargs.get('pk')
            q = test_db.objects.get(id = pk)
            q.delete()
            return HttpResponse("delete " + pk + " ok!", status = status.HTTP_200_OK)
'''