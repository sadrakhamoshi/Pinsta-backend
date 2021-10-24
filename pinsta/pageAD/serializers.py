from rest_framework import serializers
from .models import *


class PageADListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageAD
        fields = '__all__'


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


class FavoritePageAdListSerializer(serializers.ModelSerializer):
    page_ad = PageADListSerializer(source='page', read_only=True)

    class Meta:
        model = FavoritePage
        fields = ['id', 'page_ad']


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
