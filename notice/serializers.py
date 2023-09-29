from rest_framework import serializers
from .models import *

class NotificationImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    
    class Meta:
        model = Notification_image
        fields = ['image']
    

class NotificationSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

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
        fields = ['id', 'title','type','content','created_at','images']
        

        
class PromotionImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    
    class Meta:
        model = Promotion_image
        fields = ['image']
    

class PromotionSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()
     
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
        
    def get_thumbnail(self, instance):
        request = self.context.get('request')
        first_image = instance.promotionimages.first()
        if first_image:
            thumbnail_url = request.build_absolute_uri(first_image.image.url)
            return thumbnail_url
        return None
    
    class Meta:
        model = Promotion
        fields = ['id', 'title','type','content','created_at','images', 'thumbnail']