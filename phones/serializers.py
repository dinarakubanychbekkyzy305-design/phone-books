# phones/serializers.py
from rest_framework import serializers
from .models import Phone

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['title', 'author', 'year', 'cover', 'is_available']
