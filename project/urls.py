from django.urls import path
from . import views

app_name = 'project'
urlpatterns = [
    path('', views.project_list, name='project_list')
]

