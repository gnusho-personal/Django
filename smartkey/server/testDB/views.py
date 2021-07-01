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
        '''
        b = request.body.decode('utf-8')
        if len(b) == 0: b = '{}'
        json_body = json.loads(b)
        '''
        '''
        test_db(
            test_char = json_body['test_char'],
            test_email = json_body['test_email'],
            test_integer = json_body['test_integer'],
            test_float = json_body['test_float']
        ).save()
        '''

        #test_serializer = TestSerializer(data = request.data)

        data = JSONParser().parse(request)
        print(data)
        test_serializer = TestSerializer(data = data)

        if test_serializer.is_valid():
            test_serializer.save()
            return HttpResponse(test_serializer.data, status = status.HTTP_200_OK)
        else:
            return HttpResponse(test_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    # Get
    def get(self, request, **kwargs):

        ret = 'Hello World Get'
        if kwargs.get('pk') is not None:
            pk = kwargs.get('pk')
            ret += ' ' + str(pk)
        
        a = request.GET.get('a', -1)
        ret += ' ' + str(a)
        
        response = HttpResponse(ret, status = status.HTTP_200_OK)

        return response
    
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