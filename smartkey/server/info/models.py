# -*- coding: utf-8 -*-
from django.core.validators import RegexValidator
from django.db import models
import os

class Contractor(models.Model):
    '''
    시행사 model
    상호명: business name
    주소: address
    전화번호: call

    callRegex는 call의 valid 여부 검사를 위한 정규표현식입니다.
    '''
    business_name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 50)
    callRegex = RegexValidator(regex = r'^\+?1?\d{8,15}$')
    call = models.CharField(validators = [callRegex], max_length = 16, unique = True)

class SalesAgent(models.Model):
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

