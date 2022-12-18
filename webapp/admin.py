import datetime

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput
from django.core.mail import send_mail, BadHeaderError
from .models import *
from django.contrib.auth.models import Group
from django.contrib.admin import register


class FileInlineAdmin(admin.TabularInline):
    model = file


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

    inlines = [FileInlineAdmin, ]



@register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    exclude = ["last_login", "groups", "user_permissions", "is_superuser"]
    fields = ("username", "email", "password", "full_name", "department_user", "birthday", "access")
    # add_form = UserCreationForm
    def save_model(self, request, obj, form, change):
        if obj.register_time == None:
            send_mail(f"Здраствуйте, {obj.full_name}.",
                      f"Вы были зарегестрированны на <Название сайта>\n Ваш пароль: {obj.password}",
                      'bombino2281337test@gmail.com',[obj.email])
        obj.save()


admin.site.register(file, Web)
admin.site.register(folder, Web_2)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
