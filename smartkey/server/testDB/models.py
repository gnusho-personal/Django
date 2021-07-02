from django.db import models
import os

class test_db(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    test_char = models.CharField(max_length = 30)
    test_email = models.EmailField(max_length = 254)
    test_integer = models.IntegerField()
    test_float = models.IntegerField()

    def __str__(self):
        return f'[{self.pk}] {self.test_char}'
    
