from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.EmailField(max_length=64)
    password = models.CharField(max_length=64)
    date = models.DateTimeField()

class NewsData(models.Model):
    category = models.CharField(max_length=64)
    news_name = models.CharField(max_length=256)
    news_href = models.CharField(max_length=256)

class UserInfo(models.Model):
    nickname = models.CharField(max_length = 64)
    Email = models.EmailField(max_length=64)
    phone_number = models.CharField(max_length=64)
    Identity_Verification = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    api_key = models.CharField(max_length=256)
    sec_key = models.CharField(max_length=256)
    last_login = models.DateTimeField(null=True)