from rest_framework import serializers
from .models import Chat

class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ['id', 'content', 'created_at', 'icon', 'key']
        read_only_field = ['id', 'created_at']