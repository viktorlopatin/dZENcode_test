from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import CommentForm
from .models import *
from django.views.generic import ListView, DetailView
from .config import *


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
        post = Post.get_by_id(1)

        sort = self.request.GET["sort"] if "sort" in self.request.GET else None
        page = self.request.GET["page"] if "page" in self.request.GET else 1

        pg = Paginator(post.comments(sort), PAGE_SIZE)
        comments = pg.get_page(page)

        context['form_comment'] = CommentForm()
        context['comments'] = comments
        context["num_pages"] = range(1, pg.num_pages+1) if pg.num_pages > 1 else None
        if sort:
            context["sort"] = sort
        if page:
            context["page"] = page
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
        else:
            return render(request, 'comments/invalid_form.html', {"error": form.errors})
