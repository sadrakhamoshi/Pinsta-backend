from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import PageAD, FavoritePage
from .serizlizers import *
from django.db.models import Q


class PageADViewSet(ModelViewSet):
    serializer_class = PageADListSerializer
    queryset = PageAD.objects.all()

    def get_queryset(self):
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
