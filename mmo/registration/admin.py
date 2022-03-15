from django.contrib import admin
from django.utils.html import format_html  # для отображения фото в админке
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width: 50px; height: 50px;"/>'.format(obj.avatar.url))
    image_tag.short_description = 'изображение'

    list_display = ['user', 'birthdate', 'image_tag', 'first_name', 'last_name', 'email']