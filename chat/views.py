from django.shortcuts import render
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from .models import *
from .serializers import ChatSerializer
from rest_framework.response import Response
from .paginations import ChatPagination
# Create your views here.

class ChatViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    # queryset 가져오는 함수 오버라이딩 (최신순으로 정렬)
    def get_queryset(self):
        queryset = Chat.objects.all().order_by('created_at')
        return queryset
    serializer_class = ChatSerializer
    pagination_class = ChatPagination

    def create(self, reqest):
        serializer = self.get_serializer(data=reqest.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # 방명록의 왼쪽 열에 대한 api
    @action(detail=False, methods=['GET'], url_path='dataleft')
    def dataleft(self, request):
        # id가 홀수인 방명록만 가져오기
        dataleft = self.get_queryset().extra(where=["id % 2 = 1"]) 
        serializer = self.get_serializer(dataleft, many=True)
        return Response(serializer.data)
    
    # 방명록의 오른쪽 열에 대한 api
    @action(detail=False, methods=['GET'], url_path='dataright')
    def dataright(self, request):
        # id가 짝수인 방명록만 가져오기
        dataright = self.get_queryset().extra(where=["id % 2 = 0"]) 
        serializer = self.get_serializer(dataright, many=True)
        return Response(serializer.data)