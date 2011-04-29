from django.db import models
from django.contrib import admin

from dddm.session.models import Session, Slot


class SessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'excerpt', 'speaker', 'slot', 'room', 'is_break',)
    search_fields = ('title', 'description',)
    list_filter = ('room', 'slot',)


class SlotAdmin(admin.ModelAdmin):
    list_display = ('start', 'end',)


admin.site.register(Session, SessionAdmin)
admin.site.register(Slot, SlotAdmin)
