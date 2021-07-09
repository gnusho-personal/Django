# -*- coding: utf-8 -*-
'''
현재 나와있는 field들의 추가적인 옵션은 진행하면서 수정해 나갈 것
(option + validator + choice 등등)
'''
from django.core.validators import RegexValidator
from django.db import models
import os, re

class Contractors(models.Model):
    '''
    [시행사 model]
    상호명: business name
    주소: address
    전화번호: call

    callRegex는 call의 valid 여부 검사를 위한 정규표현식.
    '''
    business_name = models.CharField(max_length = 50)
    # 주소와 관련된 form은 정부에서 지정한 form이 있긴 함
    # 문제는 그 form을 정부조차 지키지 않는 것
    # 우선은 그냥 charfield로 받는게 타당하다고 생각이 듬
    address = models.CharField(max_length = 50)
    callRegex = RegexValidator(regex = r'^\d{2,3}-\d{3,4}-\d{4}$')
    call = models.CharField(validators = [callRegex], max_length = 16, unique = True)

class Sales_Agents(models.Model):
    '''
    판매 대리점 모델
    상호명: business name
    주소: address
    전화번호: call

    callRegex는 call의 valid 여부 검사를 위한 정규표현식입니다.
    '''
    business_name = models.CharField(max_length = 50)
    # 주소와 관련된 form은 정부에서 지정한 form이 있긴 함
    # 문제는 그 form을 정부조차 지키지 않는 것
    # 우선은 그냥 charfield로 받는게 타당하다고 생각이 듬
    address = models.CharField(max_length = 50)
    # 휴대폰일수도 아직 전화를 사용하고 있을 수 있으므로
    callRegex = RegexValidator(regex = r'^\d{2,3}-\d{3,4}-\d{4}$')
    call = models.CharField(validators = [callRegex], max_length = 10)

class Products(models.Model):
    '''
    [상품 model]
    serial_number: 일련번호, 상품번호
    created_at: 이 제품이 최초로 등록된 datetime
    
    bluetooth_MAC: 블루투스 MAC address
    smartdoor_MAC: 스마트 도어 전용 블루투스 MAC address
    passoword: 제품 사용할 때 쓰는 비밀번호
    
    lineup: 제품의 종류
    status: 현재 상태

    firmware_ver: 어떤 버전의 펌웨어를 사용중인지
    
    buyerID: 제품을 최초로 구매한 사람 ID
    
    contractor -> foreign key
    sales_agent -> foreign key
    '''

    # serial number 만드는 규칙을 정해야함
    serial_number = models.CharField(max_length = 30, primary_key = True)
    created_at = models.DateTimeField(auto_now_add = True)
    
    MACRegex = RegexValidator(regex = r'^((\w){2}:){5}\w{2}$')
    bluetooth_MAC = models.CharField(validators = [MACRegex], max_length = 18, unique = True)
    smartdoor_MAC = models.CharField(validators = [MACRegex], max_length = 18, unique = True)
    password = models.CharField(max_length = 17)

    # lineup 과 status는 choice를 사용해서 구현할 예정
    DEVICE_CHOICES = (
        ('TS', 'tikeytaka single'),
        ('TD', 'tikeyyaka dual'),
        ('KP', 'keyfreecar premium'),
        ('KC', 'keyfreecar connected'),
        ('KL', 'keyfreecar connected lite'),
    )
    lineup = models.CharField(max_length = 2, choices = DEVICE_CHOICES)
    
    # STATUS 관련해서는 향후 정확한 사항을 정리해서 수정할 것
    # 대분류, 소분류로 나눌지와 그 이후의 방식도 생각해야함
    STATUS_CHOICES = (
        ('P', 'production'),
        ('M', 'movement'),
        ('S', 'sell'),
    )
    status = models.CharField(max_length = 2, choices = STATUS_CHOICES)

    # Firmware version의 정확한 form 확인 할 것
    firmware_ver = models.CharField(max_length = 25)

    buyerID = models.CharField(max_length = 15)

    contractor = models.ForeignKey(Contractors, null = True, on_delete = models.SET_NULL)
    sales_agent = models.ForeignKey(Sales_Agents, null = True, on_delete = models.SET_NULL)

class Car_Infos(models.Model):
    '''
    [자동차 정보 model]
    해당 일련번호의 키를 사용하는 자동차들의 정보를 나타내는 table
    product -> foreign key
    
    car_number: 주소와 4자리 수의 번호를 포함한 자동차 번호
    
    car_company: 자동차 회사
    car_type: 자동차 기종
    car_year: 자동차 연식
    '''
    # 제품을 교체하는 상황을 위해서 null = True/ on_delete = SET_NULL로 설정함
    # 문제가 생기면 수정을 할 수 있는 기능을 줄지 아니면 싹다 지우고 다시 등록하게 할지 고민해봐야 함
    product = models.ForeignKey(Products, null = True, on_delete = models.SET_NULL)

    number = models.CharField(max_length = 20, primary_key = True)
    year = models.CharField(max_length = 4)
    # car type은 choice를 사용해서 구현할 예정
    # 관련자료 올 때까지 우선 charfield로 사용
    car_type = models.CharField(max_length = 20)

class Update_Logs(models.Model):
    '''
    [상품관련 로그 저장 model]
    상태에 따라서 달라지는 값들을 저장하는 table

    date: update 시간 miliseconds 단위까지의 시간을 나타냄

    action: status와 동일
    before: json 형태로 정리된 이전 값
    after: json 형태로 정리된 이후 값

    product -> foreign key
    '''
    product = models.ForeignKey(Products, null = True, on_delete = models.SET_NULL)

    date = models.DateTimeField(auto_now_add = True, primary_key = True)

    # ACTION 관련해서는 향후 정확한 사항을 정리해서 수정할 것
    # 대분류, 소분류로 나눌지와 그 이후의 방식도 생각해야함
    # product의 action과 계를 같이 함
    ACTION_CHOICES = (
        ('P', 'production'),
        ('M', 'movement'),
        ('S', 'sell'),
    )

    action = models.CharField(max_length = 2, choices = ACTION_CHOICES)

    before = models.JSONField()
    after = models.JSONField()

class Users_Products(models.Model):
    '''
    [이용자와 상품 match model]
    어떤 이용자가 어떤 상품을 사용하는지 M:N관계의 table

    userID: 이용자의 ID (app에서)
    product -> foreign keyx
    '''
    userID = models.CharField(max_length = 30)
    product = models.ForeignKey(Products, null = True, on_delete = models.SET_NULL)

class Feedbacks(models.Model):
    '''
    [피드백 model]
    이용자로부터 받은 피드백을 저장하기 위한 model

    contents: 피드백 내용
    results: 피드백에 대응한 내용

    user_product: 무슨 상품에 대한 어떤 이용자의 피드백인지에 대한 내용
    '''
    contents = models.TextField()
    results = models.TextField()

    user_product = models.ForeignKey(Users_Products, null = True, on_delete = models.SET_NULL)
