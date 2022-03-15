from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('registration.urls'))  # добавлено самостоятельно для первичного перехода на страницы рег-ции и пр.
]
