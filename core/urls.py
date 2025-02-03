from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path('service/<slug:slug>/', views.service_detail, name='service_detail'),
    path('contact/', views.contact, name='contact'),
]
