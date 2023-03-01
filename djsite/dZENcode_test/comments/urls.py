from django.urls import path

from .views import *

urlpatterns = [
    path('', ShowPosts.as_view(), name='index'),
]
