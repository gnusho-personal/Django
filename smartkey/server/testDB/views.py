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
