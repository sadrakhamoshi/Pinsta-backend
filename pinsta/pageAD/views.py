from datetime import datetime
from datetime import timedelta
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serizlizers import *
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .permissions import *
from django.db.models import Q
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import AnonymousUser


class PageADViewSet(ModelViewSet):
    serializer_class = PageADListSerializer
    queryset = PageAD.objects.all()

    permission_classes = [PageAdPermissions, ]

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return super(PageADViewSet, self).get_queryset()
        if self.action == 'list':
            return self.queryset.exclude(owner=self.request.user)
        return super(PageADViewSet, self).get_queryset()

    def get_serializer_class(self):
        if self.action == 'create':
            return PageADCreateSerializer
        return self.serializer_class

    def get_my_page(self, request, *args, **kwargs):
        datas = self.queryset.filter(owner=request.user)
        return Response({'pages': self.serializer_class(datas, many=True).data}, status=status.HTTP_200_OK)

    def get_page_up_to_now(self, request, *args, **kwargs):
        query = self.queryset.exclude(owner=request.user).filter(deadline__gt=datetime.now())
        return JsonResponse(PageADListSerializer(query, many=True).data, safe=False, status=status.HTTP_200_OK)

    def search(self, request, *args, **kwargs):
        result_data = self.queryset.exclude(owner=request.user)
        query_params = request.query_params
        condition = Q()
        if query_params.get('username'):
            condition = Q(username_insta__icontains=query_params.get('username'))
        keys = ['category', 'sub_category']
        for k in keys:
            if query_params.get(k):
                condition.add(Q(**{k: query_params.get(k)}), Q.AND)
        result = result_data.filter(condition)
        return Response({'pages': self.serializer_class(result, many=True).data}, status=status.HTTP_200_OK)


class FavoritePagesViewSet(ModelViewSet):
    queryset = FavoritePage.objects.all()
    serializer_class = FavoritePageAdSerializer
    permission_classes = [FavoritePagePermission, ]

    def get_my_favorite(self, request, *args, **kwargs):
        favorites = self.queryset.filter(user=request.user)
        return JsonResponse(self.serializer_class(favorites, many=True).data, safe=False, status=status.HTTP_200_OK)


class PageAdRequestViewSet(ModelViewSet):
    queryset = PageAdRequest.objects.all()
    serializer_class = RequestPageAdSerializer

    permission_classes = [PageAdRequestPermission, ]

    def accept(self, request, *args, **kwargs):
        request_page_ad = get_object_or_404(self.queryset, id=kwargs.get('pk'))
        pageAd = request_page_ad.page_ad
        if request_page_ad.membership == PageAdRequest.WEEK:
            days = 7
        elif request_page_ad.membership == PageAdRequest.MONTH:
            days = 30
        else:
            days = 365
        pageAd.deadline = datetime.now() + timedelta(days=days)
        pageAd.save()
        request_page_ad.delete()
        return JsonResponse({'msg': 'successfully accepted'}, safe=False, status=status.HTTP_200_OK)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser, ]
    serializer_class = CategorySerializer


class SubCategoryViewSet(ModelViewSet):
    permission_classes = [IsAdminUser, ]
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        query_params = self.request.query_params.get('category')
        return SubCategory.objects.all().filter(category__name=query_params)
