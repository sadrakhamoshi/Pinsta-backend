from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import PageAD, FavoritePage
from .serizlizers import *


class PageADViewSet(ModelViewSet):
    serializer_class = PageADListSerializer
    queryset = PageAD.objects.all()

    def get_queryset(self):
        if self.action == 'list':
            return PageAD.objects.all().exclude(owner=self.request.user)
        return self.queryset

    def get_serializer_class(self):
        if self.action == 'create':
            return PageADCreateSerializer
        return self.serializer_class

    def get_my_page(self, request, *args, **kwargs):
        datas = self.queryset.filter(owner=request.user)
        return Response({'pages': self.serializer_class(datas, many=True).data}, status=status.HTTP_200_OK)
