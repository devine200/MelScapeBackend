from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html')

def faq(request):
    return render(request, 'faq.html')

def blog(request):
    return render(request, 'blog.html')

def blog_details(request):
    return render(request, 'blog-single.html')

def contact(request):
    return render(request, 'contact-us.html')

def privacy_policy(request):
    return render(request, 'privacy-policy.html')