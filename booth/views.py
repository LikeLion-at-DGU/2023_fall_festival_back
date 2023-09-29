import secrets

from django.utils import timezone
from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import Extract
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Booth, Booth_like
from .serializers import BoothListSerializer, BoothSerializer, LikeSerializer
from .paginations import BoothPagination

class BoothFilter(filters.FilterSet):
    date = filters.NumberFilter(field_name='date')

    class Meta:
        model = Booth
        fields = ['location', 'type', 'date']

class BoothViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):

    pagination_class = BoothPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = BoothFilter
    
    def get_queryset(self):
        queryset = Booth.objects.annotate(
            like_cnt = Count('likes'),
            date = Extract('start_at', 'day')
            
        ) 
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return BoothListSerializer
        return BoothSerializer
    
    # 핫부스 TOP3
    @action(methods=['GET'], detail=False)
    def hot(self, request):
        current_time = timezone.now()
        top3 = self.get_queryset().filter(start_at__lte=current_time, end_at__gte=current_time).order_by('-like_cnt')[:3]
        top3_serializer = BoothListSerializer(top3, many=True, context = {'request': request})
        return Response( top3_serializer.data )

    # 좋아요
    @action(methods=['POST', 'DELETE'], detail=True)
    def likes(self, request, pk=None):
        booth = self.get_object()
        booth_id = str(booth.id)

        if request.method == 'POST':
            if booth_id in request.COOKIES.keys():
                return Response({'error': '이미 좋아료를 눌렀습니다.'}, status=status.HTTP_400_BAD_REQUEST)
            key = secrets.token_hex(5)  # 10자리 16진수 난수 생성 
            booth_like = Booth_like.objects.create(booth=booth, key=key)
            serializer = LikeSerializer(booth_like)
            response = Response(serializer.data)
            response.set_cookie(booth_id, key, max_age=2*60*60) # 쿠키 만료기간 2일
            
            return response
        
        elif request.method == 'DELETE':
            # cookie가 booth_id를 가지고 있지 않 경우
            if booth_id not in request.COOKIES.keys():
                return Response({'error': '좋아요를 누르지 않았습니다.'}, status=status.HTTP_400_BAD_REQUEST)
            
            key = request.COOKIES[booth_id]
            booth_like = Booth_like.objects.filter(booth=booth, key=key)

            if booth_like.exists():
                booth_like.delete()
                response = Response({'message' : '좋아요 취소, 쿠키 삭제'})
                response.delete_cookie(str(booth_id))
                return response
            else:
                return Response({'error': '해당 부스에 대한 좋아요를 찾을 수 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)