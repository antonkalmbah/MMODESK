from django.apps import AppConfig
from django.db.models.signals import post_save
from django.dispatch import receiver


# class AccountsConfig(AppConfig):
#     name = 'accounts'
#
#     # нам надо переопределить метод ready,
#     # чтобы при готовности нашего приложения импортировался модуль со всеми функциями обработчиками
#     def ready(self):
#         import registration.signals