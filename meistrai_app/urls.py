from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'gallery', views.gallery, name='gallery'),
    url(r'contact', views.contact, name='contact'),
    url(r'about', views.about, name='about'),
    url(r'services', views.services, name='about'),

]
