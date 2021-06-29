from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
import json

def print_request_log(request):
    print(request)

    print(request.META.items())
    # Meta에는 header의 모든 내용이 저장되있음
    # 위의 코드를 사용시 모든 item들을 tuple 형태로 print할 수 있음

    b = request.body.decode('utf-8')
    if len(b) == 0: b = '{}'
    json_body = json.loads(b)
    print('Body : ', json.dumps(json_body, indent="\t"))
    # 보통은 serializer를 이용해서 구현
    # 현재는 model이 만들어지지 않았으니까 우선은 이렇게 사용
    

class Hello_World(APIView):
    #Post
    def post(self, request):
        a = request.GET.get('a', -1)
        print_request_log(request)

        res = HttpResponse('Hello World Post', status = status.HTTP_200_OK)
        #print(res.headers)
        #print(res.content)
        #print(res.status_code)
        return res

    #Get
    def get(self, request, **kwargs):
        ret = 'Hello World Get'
        if kwargs.get('pk') is not None:
            pk = kwargs.get('pk')
            ret += ' ' + str(pk)
        
        a = request.GET.get('a', -1)
        ret += ' ' + str(a)

        #print_request_log(request)

        return Response(ret, status = status.HTTP_200_OK)

    #Put
    def put(self, request, **kwargs):
        ret = 'Hello World Put'
        if kwargs.get('pk') is not None:
            pk = kwargs.get('pk')
            ret += ' ' + str(pk)

        a = request.GET.get('a', -1)
        print(a)
        #body = json.loads(request.body)
        #print(body)
        return Response(ret, status = status.HTTP_200_OK)

    #Delete
    def delete(self, request, **kwargs):
        ret = 'Hello World Del'
        if kwargs.get('pk') is not None:
            pk = kwargs.get('pk')
            ret += ' ' + str(pk)
        a = request.GET.get('a', -1)
        print(a)
        #body = json.loads(request.body)
        #print(body)
        return Response(ret, status = status.HTTP_200_OK)
