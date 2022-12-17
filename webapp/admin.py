from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput

from .models import *
from django.contrib.auth.models import Group
from django.contrib.admin import register

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

@register(User)
class UserAdmin(admin.ModelAdmin):
    # exclude = ["last_login", "groups", "user_permissions", "is_superuser"]
    fields = ("username", "email", "password", "full_name", "department_user", "birthday", "access")

admin.site.register(file, Web)
admin.site.register(folder, Web_2)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)