from datetime import datetime
from datetime import timedelta
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serizlizers import *
from django.http import JsonResponse

from rest_framework.permissions import IsAdminUser
from django.db.models import Q
from django.contrib.auth.models import AnonymousUser


class PageADViewSet(ModelViewSet):
    serializer_class = PageADListSerializer
    queryset = PageAD.objects.all()

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return super(PageADViewSet, self).get_queryset()
        return self.queryset.exclude(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return PageADCreateSerializer
        return self.serializer_class

    def get_my_page(self, request, *args, **kwargs):
        datas = self.queryset.filter(owner=request.user)
        return Response({'pages': self.serializer_class(datas, many=True).data}, status=status.HTTP_200_OK)

    def search(self, request, *args, **kwargs):
        result_data = self.get_queryset()
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
    pass


class PageAdRequestViewSet(ModelViewSet):
    queryset = PageAdRequest.objects.all()
    serializer_class = RequestPageAdListSerializer

    # TODO add permission class for admin and normal users
    # permission_classes = [IsAdminUser, ]

    def get_serializer_class(self):
        if self.action == "create":
            return RequestPageAdSerializer
        return self.serializer_class

    def accept(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        request_page_ad = self.queryset.get(id=id)
        pageAd = request_page_ad.page_ad
        if request_page_ad.membership == 'w':
            days = 7
        elif request_page_ad.membership == 'm':
            days = 30
        else:
            days = 365
        pageAd.deadline = datetime.now() + timedelta(days=days)
        pageAd.save()
        request_page_ad.delete()
        return JsonResponse({'msg': 'successfully accepted'}, safe=False, status=status.HTTP_200_OK)
