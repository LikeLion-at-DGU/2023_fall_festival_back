from django.shortcuts import render
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from .models import *
from .serializers import ChatSerializer
from rest_framework.response import Response
from .paginations import ChatPagination
# Create your views here.

class ChatViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin):

    def get_queryset(self):
        return Chat.objects.all()
    
    serializer_class = ChatSerializer
    pagination_class = ChatPagination

    # @action(detail=False, methods=['GET'], url_path='dataleft')
    # def dataleft(self, request):
    #     dataleft = self.get_queryset().filter
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)