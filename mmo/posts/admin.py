from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


# from .models import Post


# добавлено для работы редактора ckeditor в admin-панели до ------------------------

# class PostAdminForm(forms.ModelForm):
#     description = forms.CharField(widget=CKEditorUploadingWidget())
#
#     class Meta:
#         model = Post
#         fields = '__all__'
#
#
# class PostAdmin(admin.ModelAdmin):
#     form = PostAdminForm
#     list_display = ('title', 'description')
#
# # ------------------------
#
#
# admin.site.register(Post, PostAdmin)

from django.contrib import admin
from django.utils.html import format_html  # для отображения фото в админке
from .models import *


@admin.register(Post)
class BoardAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width: 50px; height: 50px;"/>'.format(obj.image.url))
    image_tag.short_description = 'изображение'

    date_hierarchy = 'created'
    list_display = ['name', 'description', 'created', 'image_tag', 'url', 'content', 'owner']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'body', 'email', 'created', 'active']
    list_filter = ['post', 'created', 'body', 'active']
    search_fields = ['name', 'email', 'body', 'active']
