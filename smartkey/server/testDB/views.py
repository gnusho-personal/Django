from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import test_db
import json, datetime, logging, time

logger = logging.getLogger(__name__)

class TestDB(APIView):
    '''
    json body info
    {
        "test_char": "Super hero squad",
        "test_email": "osj2387@naver.com",
        "test_integer": 2016024893,
        "test_float": 3.141592,
    }
    '''

    # Post
    def post(self, request):
        # body에서 정보를 뽑아와서 object를 save할 예정
        b = request.body.decode('utf-8')
        if len(b) == 0: b = '{}'
        json_body = json.loads(b)
        #json_body = json.dumps(json_body_tmp, indent='\t')

        #print("\n\n\n\n")
        #print(json_body)
        #print("\n\n\n\n")

        test_db(
            test_char = json_body['test_char'],
            test_email = json_body['test_email'],
            test_integer = json_body['test_integer'],
            test_float = json_body['test_float']
        ).save()

        response = HttpResponse("well post", status = status.HTTP_200_OK)

        return response

    '''
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