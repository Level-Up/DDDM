from django.db import models
from django.contrib import admin

from dddm.account.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'website', 'twitter',)
    search_fields = ('company', 'bio', 'twitter',)


admin.site.register(UserProfile, UserProfileAdmin)
