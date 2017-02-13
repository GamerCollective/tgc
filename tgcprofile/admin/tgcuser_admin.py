from django.contrib import admin
from django.contrib.admin import ModelAdmin

from ..models import TGCUser


class TGCUserModelAdmin(ModelAdmin):
    pass

admin.register(TGCUser, TGCUserModelAdmin)
