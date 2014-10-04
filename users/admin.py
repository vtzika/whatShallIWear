from django.contrib import admin
from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'gender', 'location')

admin.site.register(User, UserAdmin)
