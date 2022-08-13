from django.contrib import admin
from .models import User,NewsData,UserInfo
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass

class NewsDataAdmin(admin.ModelAdmin):
    pass
class UserInfoAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserInfo,UserInfoAdmin)
admin.site.register(NewsData,NewsDataAdmin)
admin.site.register(User, UserAdmin)