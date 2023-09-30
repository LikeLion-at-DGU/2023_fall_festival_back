from rest_framework import serializers
from .models import *

# 공지(Notification)
class NotificationImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    
    class Meta:
        model = Notification_image
        fields = ['image']
        

class NotificationListSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()
    # 공지 썸네일
    def get_thumbnail(self, instance):
        request = self.context.get('request')
        first_image = instance.notificationimages.first()
        if first_image:
            thumbnail_url = request.build_absolute_uri(first_image.image.url)
            return thumbnail_url
        return None

    class Meta:
        model = Notification
        fields = ['id', 'title','type','content','thumbnail']
    

class NotificationSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    # 공지 게시일
    def get_date(self, instance):
        start = str(instance.created_at)
        date = start[:4] + '.' + start[5:7] + '.' + start[8:10]
        return date
    # 공지 다중 이미지
    def get_images(self, instance):
        request=self.context.get('request')
        noticeimage=instance.notificationimages.all().order_by('id')
        try:
            noticeimage_serializer=NotificationImageSerializer(noticeimage, many=True)
            outcome = []
            for data in noticeimage_serializer.data:
                image_url = request.build_absolute_uri(data["image"])
                outcome.append(image_url)
            return outcome
        except:
            return None
    
    class Meta:
        model = Notification
        fields = ['id', 'title','type','content','date','images']
        


# 홍보(Promotion)       
class PromotionImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    
    class Meta:
        model = Promotion_image
        fields = ['image']
       
        
class PromotionListSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()
    # 홍보 썸네일
    def get_thumbnail(self, instance):
        request = self.context.get('request')
        first_image = instance.promotionimages.first()
        if first_image:
            thumbnail_url = request.build_absolute_uri(first_image.image.url)
            return thumbnail_url
        return None

    class Meta:
        model = Notification
        fields = ['id', 'title','type','content','thumbnail']
    

class PromotionSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    # 홍보 게시일
    def get_date(self, instance):
        start = str(instance.created_at)
        date = start[:4] + '.' + start[5:7] + '.' + start[8:10]
        return date
    # 홍보 다중 이미지
    def get_images(self, instance):
        request=self.context.get('request')
        promoteimage=instance.promotionimages.all().order_by('id')
        try:
            promoteimage_serializer=PromotionImageSerializer(promoteimage, many=True)
            outcome = []
            for data in promoteimage_serializer.data:
                image_url = request.build_absolute_uri(data["image"])
                outcome.append(image_url)
            return outcome
        except:
            return None
        
    class Meta:
        model = Promotion
        fields = ['id', 'title','type','content','date','images']