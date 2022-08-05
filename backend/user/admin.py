from django.contrib import admin
from .models import User,NewsData
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass

class NewsDataAdmin(admin.ModelAdmin):
    pass

admin.site.register(NewsData,NewsDataAdmin)
admin.site.register(User, UserAdmin)