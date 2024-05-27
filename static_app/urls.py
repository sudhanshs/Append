from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('blog-detail/<str:slug>/', views.BlogDetail, name='blog_detail'),
    path('blog-list', views.BlogList, name='blog_list'),
    path('portfolio-detail', views.PortfolioDetail, name='portfolio_detail'),
    path('services-detail', views.ServicesDetail, name='services_detail'),
    path('about-us', views.AboutUs, name='about_us'),
    path('contact-us', views.ContactUS, name='contact_us'),
    path('GivaHome', views.GivaHome, name='GivaHome'),


    ]