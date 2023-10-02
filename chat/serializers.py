from rest_framework import serializers
from .models import Chat

class ChatSerializer(serializers.ModelSerializer):
    is_abused = serializers.BooleanField(read_only=True, default=False)

    # 욕설 필터링 기능 추가 예정
    def get_is_abused(self, obj):
        return obj.is_abused
    class Meta:
        model = Chat
        fields = ['id', 'content', 'icon', 'is_abused', 'key']