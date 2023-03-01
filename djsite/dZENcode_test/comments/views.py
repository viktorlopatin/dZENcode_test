from django.shortcuts import render, redirect

from .forms import CommentForm
from .models import *
from django.views.generic import ListView, DetailView


class ShowPosts(ListView):
    model = Post
    template_name = 'comments/index.html'
    pk_url_kwarg = 'slug'
    context_object_name = 'post'
    success_url = 'comments/index.html'

    def get_queryset(self):
        return Post.get_by_id(1)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sort = self.request.GET["sort"] if "sort" in self.request.GET else None
        comments = Post.get_by_id(1).comments(sort)
        context['form_comment'] = CommentForm()
        context['comments'] = comments
        return context

    @staticmethod
    def post(request, *args, **kwargs):
        form = CommentForm(request.POST, request.FILES)
        comment_id = request.GET["comment_id"] if "comment_id" in request.GET else None

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            user = User.get_by_name_and_email(name, email)
            post = Post.get_by_id(1)

            params = {
                "text": form.cleaned_data['text'],
                "file": form.cleaned_data['file'],
                "user": user,
                "post": post
            }

            if comment_id:
                parent_comment = Comment.get_by_id(comment_id)
                params['parent_comment'] = parent_comment

            comment = Comment(**params)
            comment.save()
        return redirect('index')
