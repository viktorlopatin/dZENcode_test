from django.urls import path, include

from .views import *

urlpatterns = [
    path('', ShowPosts.as_view(), name='index'),
    path('captcha/', include('captcha.urls')),

]
