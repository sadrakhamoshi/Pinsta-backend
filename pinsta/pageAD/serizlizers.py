from rest_framework import serializers
from .models import *


class PageADListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageAD
        fields = '__all__'


class PageADCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageAD
        fields = ['id', 'username_insta', 'category', 'sub_category']

    def create(self, validated_data):
        user = self.context['request'].user
        return PageAD.objects.create(
            username_insta=validated_data['username_insta'],
            category=validated_data['category'],
            owner=user,
            sub_category=validated_data['sub_category']
        )


class FavoritePageAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoritePage
        fields = ['id', 'page']

    def create(self, validated_data):
        user = self.context['request'].user
        return FavoritePage.objects.create(
            user=user,
            page=validated_data['page']
        )


class RequestPageAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageAdRequest
        fields = ['id', 'page_ad', 'membership']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'
