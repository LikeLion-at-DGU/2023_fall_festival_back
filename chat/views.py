from django.shortcuts import render
from django.utils import timezone

from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from .models import *
from django.db.models import F, ExpressionWrapper, IntegerField
from .serializers import ChatSerializer
from rest_framework.response import Response
from .paginations import ChatPagination
from django.conf import settings

import os
from uuid import uuid4 
from datetime import timedelta

# Create your views here.

def load_swears(file_name):
    file_path = os.path.join(settings.BASE_DIR, 'static', file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        swears = file.read().splitlines()
    return swears

SWEARS = load_swears('fword_list.txt')

def censor_content(content):
    is_abused = False
    
    for swear in SWEARS:
        if swear in content:
            content = content.replace(swear, '*' * len(swear))
            is_abused = True
            
    return content, is_abused

class ChatViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    # queryset 가져오는 함수 오버라이딩 (최신순으로 정렬)
    def get_queryset(self):
        queryset = Chat.objects.all().order_by('-created_at')
        return queryset
    serializer_class = ChatSerializer
    pagination_class = ChatPagination
    throttle_scope='chat'

    def create(self, request):
        key = request.COOKIES.get('key')
        if not key:
            key = str(uuid4())

        cooltime_report = Chat.objects.filter(key=key).first()
        if cooltime_report:
            time_since_last_post = timezone.now() - cooltime_report.created_at

            # 현재 대기시간 30초로 설정
            if time_since_last_post < timedelta(seconds=30):
                return Response({'detail': '30초에 한 번만 글을 게시할 수 있습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        
        content = request.data.get('content')
        censored_content, is_abused = censor_content(content)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(key = key, content = censored_content, is_abused = is_abused)
        headers = self.get_success_headers(serializer.data)
        response = Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        # 현재 대기시간 30초로 설정
        response.set_cookie('key', key, max_age=30)
        return response

    # 방명록의 왼쪽 열에 대한 api
    @action(detail=False, methods=['GET'], url_path='dataleft')
    def dataleft(self, request):
        # id가 홀수인 방명록만 가져오기
        dataleft = self.get_queryset().annotate(odd_id=ExpressionWrapper(F('id') % 2, output_field=IntegerField())).filter(odd_id=1)
        page = self.paginate_queryset(dataleft)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(dataleft, many=True)
        return Response(serializer.data)

    
    # 방명록의 오른쪽 열에 대한 api
    @action(detail=False, methods=['GET'], url_path='dataright')
    def dataright(self, request):
        # id가 짝수인 방명록만 가져오기
        dataright = self.get_queryset().annotate(even_id=ExpressionWrapper(F('id') % 2, output_field=IntegerField())).filter(even_id=0)
        page = self.paginate_queryset(dataright)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(dataright, many=True)
        return Response(serializer.data)