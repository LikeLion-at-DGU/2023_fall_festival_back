from rest_framework import serializers
from .models import Chat

class ChatSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        key = validated_data.pop('key')
        chat = Chat.objects.create(**validated_data, key=key)
        return chat
    
    class Meta:
        model = Chat
        fields = ['id', 'content', 'icon', 'is_abused', 'key']