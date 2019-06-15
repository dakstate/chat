from django.urls import path, re_path
from . import views

urlpatterns = [
# Домашняя страница
    # path(r'^$', views.index, name='index'),
    path(r'^messages/$', views.notes_show, name='notes'),
    ]
