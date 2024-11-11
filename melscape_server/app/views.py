from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {"page_id": "5fb94d66e5e1d82f06729c39"})

def about(request):
    return render(request, 'about-us.html', {"page_id": "5fbc216e891686bd26b3139d"})

def faq(request):
    return render(request, 'faq.html', {"page_id": "5fbd60c43ba026730a410478"})

def blog(request):
    return render(request, 'blog.html', {"page_id": "5fbd873dc7da4ffbaf69273e"})

def blog_details(request):
    return render(request, 'blog-single.html', {"page_id": ""})

def contact(request):
    return render(request, 'contact-us.html', {"page_id": "5fbd7f40eeaa93622d5f498c"})

def privacy_policy(request):
    return render(request, 'privacy-policy.html', {"page_id": "5fbd873dc7da4ffbaf69273e"})