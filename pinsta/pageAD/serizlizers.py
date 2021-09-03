from rest_framework import serializers
from .models import PageAD


class PageADListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageAD
        fields = '__all__'


class PageADCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageAD
        fields = ['id', 'owner', 'username_insta', 'category', 'sub_category']
