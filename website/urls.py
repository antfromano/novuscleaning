from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('services.html', views.services, name="services"),
    path('pricing.html', views.pricing, name="pricing"),
    path('blog.html', views.blog, name="blog"),
    path('contact.html', views.contact, name="contact"),
]
