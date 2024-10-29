from django.urls import path
from .views import index, about, faq, blog, blog_details, contact, privacy_policy

urlpatterns = [
    path('', index, name="index"),
    path('about', about, name="about"),
    path('faq', faq, name="faq"),
    path('blog', blog, name="blog"),
    path('blog_details', blog_details, name="blog_details"),
    path('contact', contact, name="contact"),
    path('privacy_policy', privacy_policy, name="privacy_policy"),
]