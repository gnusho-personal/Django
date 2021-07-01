from rest_framework import serializers
from .models import test_db

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = test_db
        fields = '__all__'
