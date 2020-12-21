from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('work/', views.work, name='work'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('blogdetails/<int:id>', views.blogdetails, name='blogdetails'),



]

