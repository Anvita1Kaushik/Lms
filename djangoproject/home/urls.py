from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index, name='home'),
    path('lms',views.lms, name='lms'),
    path('docs',views.docs, name='docs'),
    path('downloads',views.downloads, name='downloads'),
    path('demo',views.demo, name='demo'),
    path('signin',views.signin, name='signin'),
    path('about',views.about, name='about'),
   
]
