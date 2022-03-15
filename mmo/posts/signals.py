from django.db.models.signals import post_save
from django.dispatch import receiver # импортируем нужный декоратор
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from registration.models import Profile
from .models import Post, Comment


@receiver(post_save, sender=Comment)
def comment_created(instance, created, **kwargs):
    if created:
        owner_email = instance.post.owner.email  # достаю email создателя объявления
        owner = instance.post.owner.username
        comment_user = instance.name
        comment_user_email = instance.email
        id_post = instance.post.pk
        link = f'http://127.0.0.1:8000/{id_post}/'

        owner_msg = EmailMultiAlternatives(
            subject=f'Появились обновления в категории на которую вы подписаны {instance.post.category}',
            from_email='eugen.eisner@gmail.com',
            to=[owner_email],
            )
        content = render_to_string('board/create_email.html', {
            'owner': owner,
            'link': link,
            'user': comment_user,
            'name': instance.post.name
            }
        )
        # email пользователю который оставил отзыв
        comment_user_msg = EmailMultiAlternatives(
            subject=f'Ваш отклик на объявление {instance.post.name} успешно отправлен',
            from_email='eugen.eisner@gmail.com',
            to=[comment_user_email],
        )
        comment_user_content = render_to_string('board/comment_user_email.html', {
            'link': link,
            'user_name': comment_user,
            'name': instance.post.name
            }
        )

        owner_msg.attach_alternative(content, "text/html")  # добавляем html
        owner_msg.send()  # отсылаем

        comment_user_msg.attach_alternative(comment_user_content, "text/html")  # добавляем html
        comment_user_msg.send()  # отсылаем


@receiver(post_save, sender=Comment)
def comment_accept(instance, **kwargs):
    if instance.active:
        comment_user = instance.name
        comment_user_email = instance.email
        id_post = instance.post.pk
        link = f'http://127.0.0.1:8000/{id_post}/'

        # email пользователю который оставил отзыв
        comment_user_msg = EmailMultiAlternatives(
            subject=f'Ваш отклик на объявление {instance.post.name} был принят',
            from_email='eugen.eisner@gmail.com',
            to=[comment_user_email],
        )
        comment_user_content = render_to_string('board/comment_accept.html', {
            'link': link,
            'user_name': comment_user,
            'name': instance.post.name
        }
                                                )

        comment_user_msg.attach_alternative(comment_user_content, "text/html")  # добавляем html
        comment_user_msg.send()  # отсылаем