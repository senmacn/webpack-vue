"""blogURL Configuration"""
from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path('article/(?P<article_id>[0-9]+)/$', views.get_article_details),
    path('get_article_list/', views.get_article_list),
]
