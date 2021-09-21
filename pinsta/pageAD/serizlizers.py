from rest_framework import serializers
from .models import PageAD, PageAdRequest


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
    pass


class RequestPageAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageAdRequest
        fields = ['page_ad', 'membership']

    def create(self, validated_data):
        user = self.context['request'].user
        return PageAdRequest.objects.create(
            user=user,
            page_ad=validated_data['page_ad'],
            membership=validated_data['membership']
        )


class RequestPageAdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageAdRequest
        fields = '__all__'
