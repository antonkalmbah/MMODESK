from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy

from .models import Profile
from .forms import ProfileEditForm
from posts.models import Post, Comment


class UserProfile(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'accounts/profile.html'
    context_object_name = 'profil'
    # queryset = Comment.objects.all()

    def get_context_data(self, **kwargs):
        id = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        # добавляю в контекст только посты определенного пользователя
        context['posts'] = Post.objects.filter(owner=self.request.user)
        context['comments'] = Comment.objects.filter(post_id=id)
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/edit.html'
    success_url = reverse_lazy('profile')