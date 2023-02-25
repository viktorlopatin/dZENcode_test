from django.urls import path

from .views import *

urlpatterns = [
    path('post/<int:post_id>/', ShowPosts.as_view(), name='index'),
]
