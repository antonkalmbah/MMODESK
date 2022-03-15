from django.urls import path
from . views import IndexView, AdView, AdCreateView, AdUpdateView, \
    AdDeleteView, ProfilPostDetailsView, comment_update, CommentDelete


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('<int:pk>/', AdView.as_view(), name='post'),
    path('<int:pk>/details/', ProfilPostDetailsView.as_view(), name='details'),
    path('add/', AdCreateView.as_view(), name='post_create'),
    path('<int:pk>/update/', AdUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', AdDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/comment-update/', comment_update, name='comment_update'),
    path('<int:pk>/comment-delete/', CommentDelete.as_view(), name='comment_delete'),
]