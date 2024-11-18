from django.urls import path
from .views import index, about, faq, blog, blog_details, contact, privacy_policy, blog_category

urlpatterns = [
    path('', index, name="index"),
    path('about', about, name="about"),
    path('faq', faq, name="faq"),
    path('blog', blog, name="blog"),
    path('blog_detail/<str:slug>', blog_details, name="blog_details"),
    path('blog_category/<str:category>', blog_category, name="blog_category"),
    path('contact', contact, name="contact"),
    path('privacy_policy', privacy_policy, name="privacy_policy"),
]