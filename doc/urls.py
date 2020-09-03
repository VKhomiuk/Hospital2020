from django.urls import path
from . import views
from django.contrib.flatpages import views as flat_views

urlpatterns = [
    path('', views.Doctors.as_view(), name='main'),
    path('service/', views.Service.as_view(), name='service'),
    # path('about-us/', views.AboutUs.as_view(), name='about-us'),
    path('patient/', views.News.as_view(), name='news'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('doctors/', views.Docs.as_view(), name='docs'),
    path('before/', views.Prep.as_view(), name='before'),
    path('after/', views.After.as_view(), name='after'),
    path('quest/', views.Quest.as_view(), name='quest'),
]