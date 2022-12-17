from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class Web(admin.ModelAdmin):
    list_display = ('title', 'access')
    list_display_links = ('title',)
    list_editable = ('access',)
    list_filter = ('title', 'access',)


class Web_2(admin.ModelAdmin):
    list_display = ('title', 'department')
    list_display_links = ('title',)
    list_editable = ('department',)
    list_filter = ('title', 'department',)


admin.site.register(file, Web)
admin.site.register(folder, Web_2)
admin.site.register(User)