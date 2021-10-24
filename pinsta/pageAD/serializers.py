from rest_framework import serializers
from .models import *
from account.models import User


class PageADListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageAD
        fields = '__all__'


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'avatar']


class PageAdCompleteSerializer(serializers.ModelSerializer):
    user = OwnerSerializer(source='owner', read_only=True)

    class Meta:
        model = PageAD
        fields = ['id', 'username_insta', 'description', 'deadline', 'rating', 'icon_url',
                  'category', 'sub_category', 'user']


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


class RequestPageAdListSerializer(serializers.ModelSerializer):
    pagead = PageAdCompleteSerializer(source='page_ad', read_only=True)

    class Meta:
        model = PageAdRequest
        fields = ['id', 'membership', 'pagead']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'
