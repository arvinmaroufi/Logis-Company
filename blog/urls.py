from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('<slug:slug>/', views.article_detail, name='article_detail'),
]
