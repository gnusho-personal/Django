from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
import json, datetime

def print_response_log(response):
    print('Response Done')

    header_dict = {}
    for name in response.headers:
        header_dict[name] = response.headers[name]

    json_header = json.dumps(header_dict, default=json_default, indent='\t')
    print('Header: ', json_header)

    print('Code: ', response.status_code)

    print('Body: ', response.content)

    print('Time: ', datetime.datetime.now())
    print('\n')


class Hello_World(APIView):
    #Post
    def post(self, request):

        print_request_log(request)
        a = request.GET.get('a', -1)
        response = HttpResponse('Hello World Post', status = status.HTTP_200_OK)
        print_response_log(response)

        return response

    #Get
    def get(self, request, **kwargs):

        print_request_log(request)
        
        ret = 'Hello World Get'
        if kwargs.get('pk') is not None:
            pk = kwargs.get('pk')
            ret += ' ' + str(pk)
        
        a = request.GET.get('a', -1)
        ret += ' ' + str(a)
        
        response = HttpResponse(ret, status = status.HTTP_200_OK)
        print_response_log(response)

        return Response(ret, status = status.HTTP_200_OK)

    #Put
    def put(self, request, **kwargs):

        print_request_log(request)
        ret = 'Hello World Put'
        if kwargs.get('pk') is not None:
            pk = kwargs.get('pk')
            ret += ' ' + str(pk)

        a = request.GET.get('a', -1)
        ret += ' ' + str(a)

        response = HttpResponse(ret, status = status.HTTP_200_OK)
        print_response_log(response)

        return Response(ret, status = status.HTTP_200_OK)

    #Delete
    def delete(self, request, **kwargs):

        print_request_log(request)
        ret = 'Hello World Del'
        if kwargs.get('pk') is not None:
            pk = kwargs.get('pk')
            ret += ' ' + str(pk)
        
        a = request.GET.get('a', -1)
        ret += ' ' + str(a)

        response = HttpResponse(ret, status = status.HTTP_200_OK)
        print_response_log(response)

        return Response(ret, status = status.HTTP_200_OK)

def json_default(value): 
    if isinstance(value, datetime.date): 
        return value.strftime('%Y-%m-%d')
    elif isinstance(value, tuple):
        return ''.join(value)
    elif isinstance(value, bool):
        return str(value)
    elif isinstance(value, object):
        return str(value)
    raise TypeError('not JSON serializable')

def print_request_log(request):
    print('Request Start')
    
    full_url = str(request.method) + str(request.get_full_path())
    print('URL: ', full_url)

    header_dict = {}
    for name in request.headers:
        header_dict[name] = request.headers[name]

    json_header = json.dumps(header_dict, default=json_default, indent='\t')
    print('Header: ', json_header)
    # Meta에는 header의 모든 내용이 저장되있음
    # 위의 코드를 사용시 모든 item들을 tuple 형태로 print할 수 있음

    b = request.body.decode('utf-8')
    if len(b) == 0: b = '{}'
    json_body = json.loads(b)
    print('Body: ', json.dumps(json_body, indent='\t'))
    # 보통은 serializer를 이용해서 구현
    # 현재는 model이 만들어지지 않았으니까 우선은 이렇게 사용

    cookie_dict = {}
    for name in request.COOKIES:
        cookie_dict[name] = request.COOKIES[name]
    json_cookie = json.dumps(cookie_dict, default=json_default, indent='\t')
    print('Cookie: ', json_cookie)

    print('Time: ', datetime.datetime.now())
    print('Request Done\n')