from rest_framework import serializers
from .models import Booth, Booth_like, Booth_image

class ImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booth_image
        fields = ['image']
            

class BoothListSerializer(serializers.ModelSerializer):

    like_cnt = serializers.IntegerField()

    is_liked = serializers.SerializerMethodField()
    def get_is_liked(self, instance):
        request = self.context.get('request')
        if request:
            booth_id = str(instance.id) 
            # 쿠키의 key값들을 가져와서 booth_id가 들어있는지 확인
            return booth_id in request.COOKIES.keys()
        return False



    class Meta:
        model = Booth
        fields = [
            'id',
            'name',
            'description',
            'type',
            'location',
            'like_cnt',
            'is_liked',
        ]

class BoothSerializer(serializers.ModelSerializer):
    like_cnt = serializers.IntegerField()
    

    during = serializers.SerializerMethodField()
    def get_during(self, instance):
        start = str(instance.start_at)
        end = str(instance.end_at)
        during = start[:4] + '.' + start[5:7] + '.' + start[8:10] + ' ' + start[11:16] + '~' + end[11:16]
        return during
    
    is_liked = serializers.SerializerMethodField()
    def get_is_liked(self, instance):
        request = self.context.get('request')
        if request:
            booth_id = str(instance.id) 
            # 쿠키의 key값들을 가져와서 booth_id가 들어있는지 확인
            return booth_id in request.COOKIES.keys()
        return False
        

    class Meta:
        model = Booth
        fields = [
            'id',
            'name',
            'description',
            'type',
            'location',
            'is_liked',
            'like_cnt',
            'during'
        ]

class LikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booth_like
        fields = ['id', 'booth', 'key']