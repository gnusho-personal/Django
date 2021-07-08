# -*- coding: utf-8 -*-
from django.core.validators import RegexValidator
from django.db import models
import os

class Contractors(models.Model):
    '''
    [시행사 model]
    상호명: business name
    주소: address
    전화번호: call

    callRegex는 call의 valid 여부 검사를 위한 정규표현식.
    '''
    business_name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 50)
    callRegex = RegexValidator(regex = r'^\+?1?\d{8,15}$')
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
    address = models.CharField(max_length = 50)
    callRegex = RegexValidator(regex = r'^\+?1?\d{8,15}$')
    call = models.CharField(validators = [callRegex], max_length = 16, unique = True)

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

    다음 field들의 추가적인 옵션은 진행하면서 수정해 나갈 것
    '''

    serial_number = models.CharField(max_length = 10, primary_key = True)
    created_at = models.DateTimeField(auto_now_add = True)
    
    bluetooth_MAC = models.CharField(max_length = 25)
    smartdoor_MAC = models.CharField(max_length = 25)
    password = models.CharField(max_length = 10)

    # lineup 과 status는 choice를 사용해서 구현할 예정
    #lineup =
    #status = 

    firmware_ver = models.CharField(max_length = 25)

    buyerID = models.CharField(max_length = 15)

    contractor = models.ForeignKey(Contractors, null = True, on_delete = models.SET_NULL)
    sales_agent = models.ForeignKey(Sales_Agents, null = True, on_delete = models.SET_NULL)