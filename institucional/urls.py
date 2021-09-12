from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('advantages/', views.advantages, name='advantages'),
    path('prices/', views.prices, name='prices'),
    path('faq/', views.faq, name='faq'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]