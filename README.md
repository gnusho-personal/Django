# Django-template
서버

# 개발 환경 설정
1. Python 가상환경 설정 및 실행:
- sudo apt update && sudo apt upgrade
- sudo apt install python3-pip
- sudo apt install python3-virtualenv
- sudo virtualenv mv
- sudo apt install python3-venv
- python3 -m venv mv
- sudo python3 venv mv
- source mv/bin/activate

2. Django 설치 및 프로젝트 생성:
- sudo pip install --upgrade pip
- sudo pip install django
- sudo pip freeze >> requirements.txt
- sudo pip install -r requirements.txt
- django-admin startproject "프로젝트 이름" 
- python manage.py startapp "앱 이름"

3. Django 프로젝트 실행
- python3 manage.py runserver 0.0.0.0:8000
    - ALLOWED HOST에 해당 ip를 추가해줘야 함
    - *을 추가하면 모두 허용

4. Django Mysql 연동
- sudo apt-get install libssl-dev
- sudo apt-get install mysql-server
- sudo apt-get install mysql-client
- sudo apt-get install libmysqlclient-dev
- sudo pip install mysqlclient 

