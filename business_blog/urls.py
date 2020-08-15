from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('project/', views.project, name='project'),
    #path('blog/', views.blog, name='blog'),
    #path('blog_details/', views.blog_details, name='blog_details'),
    #path('elements/', views.elements, name='elements'),
]
