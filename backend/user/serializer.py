from rest_framework import serializers
from .models import User,NewsData,UserInfo

class UserSerialrizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id','password','date']

class NewsSerialrizer(serializers.ModelSerializer):
    class Meta:
        model = NewsData
        fields = ['category','news_name','news_href']

class UserInfoSerialrizer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['nickname','Email','phone_number','Identity_Verification','password','api_key','sec_key','last_login']

class UpdateLoginTime(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['last_login']