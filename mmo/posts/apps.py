from django.apps import AppConfig


# class BoardConfig(AppConfig):
#     name = 'board'
#
#     # нам надо переопределить метод ready,
#     # чтобы при готовности нашего приложения импортировался модуль со всеми функциями обработчиками
#     def ready(self):
#         import posts.signals