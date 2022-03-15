from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import CommentForm, PostForm


class IndexView(ListView):
    model = Post
    template_name = 'board/index.html'
    context_object_name = 'posts'
    paginate_by = 3
    ordering = '-created'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(active=True)
        return context


class AdView(DetailView, FormView):
    model = Post
    template_name = 'board/ad.html'
    context_object_name = 'ad_details'
    success_url = reverse_lazy('home')
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # достаю и переопределяю id
        id = self.kwargs.get('pk')
        # привязываю комментарий к посту
        self.object.post_id = id
        self.object.save()
        return super().form_valid(form)


class ProfilPostDetailsView(DetailView):
    model = Post
    template_name = 'board/details.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        return context


class AdCreateView(CreateView, LoginRequiredMixin):
    model = Post
    form_class = PostForm
    template_name = 'board/post_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # привязываю пользователя к посту
        self.object.owner = User.objects.get(id=self.request.user.id)
        self.object.save()
        return super().form_valid(form)


class AdUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'board/post_update.html'
    success_url = reverse_lazy('home')


class AdDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'board/post_delete.html'
    success_url = reverse_lazy('profile')


class CommentDelete(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'board/comment_delete.html'
    success_url = reverse_lazy('profile')


@login_required
def comment_update(request, pk):
    com = Comment.objects.get(id=pk)
    com.active = True
    com.save()
    return redirect(reverse_lazy('profile'))