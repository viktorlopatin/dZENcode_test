from django.shortcuts import render, redirect

from .forms import CommentForm
from .models import *
from django.views.generic import ListView, DetailView


class ShowPosts(ListView):
    model = Post
    template_name = 'comments/index.html'
    pk_url_kwarg = 'slug'
    context_object_name = 'post'

    def get_queryset(self):
        return Post.get_by_id(1)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
