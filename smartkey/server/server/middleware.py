from rest_framework.status import is_client_error, is_success
from rest_framework.response import Response
import json, re, datetime, logging
from logging.handlers import RotatingFileHandler

path = '/home/ubuntu/knocktalkHYWEP/smartkey/server/debug.log'

logger = logging.getLogger('django.request')

formatter = logging.Formatter('Time & Level: %(asctime)s;%(levelname)s\n %(message)s')

# log를 console에 print하는 handler 설정
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter)

# log를 file에 저장하면서 maxbytes만큼만 저장하고 다른 파일에 내용을 백없하는 rotatingfilehandler 설정
# backupcout 만큼 backupfile 생성 // debug.log에 .(숫자) 넣어서 파일 만들어줌 필요하면 자동으로 숫자를 뒤로 밀어줌
file_handler = RotatingFileHandler(path, maxBytes = 1024, backupCount = 5)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

class LoggingMiddleware:
    METHOD = ('GET', 'POST', 'PUT', 'PATCH', 'DELETE')

    def __init__(self, get_response):
        self.get_response = get_response
        
        self.API_URLS = [
            re.compile(r'^(.*)/api'),
            re.compile(r'^api'),
        ]

    def __call__(self, request):

        self.print_request_log(request)

        response = None
        
        if not response:
            response = self.get_response(request)
        
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        
        self.print_response_log(response)
        return response

    def json_default(self, value): 
        if isinstance(value, datetime.date): 
            return value.strftime('%Y-%m-%d')
        elif isinstance(value, tuple):
            return ''.join(value)
        elif isinstance(value, bool):
            return str(value)
        elif isinstance(value, object):
            return str(value)
        raise TypeError('not JSON serializable')

    def print_request_log(self, request):

        print('Request Start')
    
        full_url = str(request.method) + str(request.get_full_path())
        print('URL: ', full_url)

        header_dict = {}
        for name in request.headers:
            header_dict[name] = request.headers[name]

        json_header = json.dumps(header_dict, default=self.json_default, indent='\t')
        #print('Header: ', json_header)
        # Meta에는 header의 모든 내용이 저장되있음
        # 위의 코드를 사용시 모든 item들을 tuple 형태로 print할 수 있음

        b = request.body.decode('utf-8')
        if len(b) == 0: b = '{}'
        json_body_tmp = json.loads(b)
        json_body = json.dumps(json_body_tmp, indent='\t')
        #print('Body: ', json.dumps(json_body, indent='\t'))
        # 보통은 serializer를 이용해서 구현
        # 현재는 model이 만들어지지 않았으니까 우선은 이렇게 사용

        cookie_dict = {}
        for name in request.COOKIES:
            cookie_dict[name] = request.COOKIES[name]
        json_cookie = json.dumps(cookie_dict, default=self.json_default, indent='\t')
        
        print('Cookie: ', json_cookie)

        print('Time: ', datetime.datetime.now())
        
        print('Request Done\n')

    def print_response_log(self, response):
        print('Response Done')

        header_dict = {}
        for name in response.headers:
            header_dict[name] = response.headers[name]

        json_header = json.dumps(header_dict, default=self.json_default, indent='\t')
        print('Header: ', json_header)

        print('Code: ', response.status_code)

        print('Body: ', response.content)

        print('Time: ', datetime.datetime.now())
        print('\n')

    def process_response(self, request, response):
        """
        API_URLS 와 method 가 확인이 되면
        response 로 들어온 data 형식에 맞추어
        response_format 에 넣어준 후 response 반환
        """
        path = request.path_info.lstrip('/')
        valid_urls = (url.match(path) for url in self.API_URLS)

        if request.method in self.METHOD and any(valid_urls):
            response_format = {
                'success': is_success(response.status_code),
                'result': {},
                'message': None
            }

            if hasattr(response, 'data') and getattr(response, 'data') is not None:
                data = response.data
                try:
                    response_format['message'] = data.pop('message')
                except (KeyError, TypeError):
                    response_format.update({
                        'result': data
                    })
                finally:
                    if is_client_error(response.status_code):
                        response_format['result'] = None
                        response_format['message'] = data
                    else:
                        response_format['result'] = data

                    response.data = response_format
                    response.content = response.render().rendered_content
            else:
                response.data = response_format

        return response
