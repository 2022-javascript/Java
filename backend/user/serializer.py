from rest_framework import serializers
from .models import User,NewsData

class UserSerialrizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id','password','date']

class NewsSerialrizer(serializers.ModelSerializer):
    class Meta:
        model = NewsData
        fields = ['category','news_name','news_href']