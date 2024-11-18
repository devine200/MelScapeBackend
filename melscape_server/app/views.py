from django.shortcuts import render
from django.http import HttpResponseNotFound
from app.models import (
    SiteInfo,
    LandingHeroSection,
    AboutHeroSection,
    CTADescription,
    CoreService,
    StepsToEarn,
    InstagramPost,
    AboutIntroSection,
    HowWeCanHelpSection,
    FAQ,
    FAQCategory,
    BlogPost,
    BlogCategory,
    BlogComment,
    ContactInfo,
)


def index(request):
    site_info = SiteInfo.objects.last()
    hero_section = LandingHeroSection.objects.last()
    cta_descriptions = CTADescription.objects.all()
    core_services = CoreService.objects.all()
    steps_to_earns = StepsToEarn.objects.all()
    recent_faqs = FAQ.objects.all()[:6]
    post1, post2, post3, post4 = InstagramPost.objects.all()

    return render(
        request,
        "index.html",
        {
            "page_id": "5fb94d66e5e1d82f06729c39",
            "site_info": site_info,
            "hero_section": hero_section,
            "cta_descriptions": cta_descriptions,
            "core_services": core_services,
            "steps_to_earns": steps_to_earns,
            "post1": post1,
            "post2": post2,
            "post3": post3,
            "post4": post4,
            "recent_faqs": recent_faqs,
        },
    )


def about(request):
    site_info = SiteInfo.objects.last()
    hero_section = AboutHeroSection.objects.last()
    post1, post2, post3, post4 = InstagramPost.objects.all()
    about_intro = AboutIntroSection.objects.last()
    use_cases = HowWeCanHelpSection.objects.all()

    return render(
        request,
        "about-us.html",
        {
            "page_id": "5fbc216e891686bd26b3139d",
            "site_info": site_info,
            "hero_section": hero_section,
            "post1": post1,
            "post2": post2,
            "post3": post3,
            "post4": post4,
            "about_intro": about_intro,
            "use_cases": use_cases,
        },
    )


def faq(request):
    site_info = SiteInfo.objects.last()
    faq_categories = FAQCategory.objects.all()
    return render(
        request,
        "faq.html",
        {
            "page_id": "5fbd60c43ba026730a410478",
            "site_info": site_info,
            "faq_categories": faq_categories,
        },
    )


def blog(request):
    site_info = SiteInfo.objects.last()
    post1, post2, post3, post4 = InstagramPost.objects.all()
    blog_posts = BlogPost.objects.all().order_by("-created_at")
    featured_blogs = BlogPost.objects.filter(is_featured=True).order_by("-created_at")[
        :3
    ]
    blog_categories = BlogCategory.objects.all()

    return render(
        request,
        "blog.html",
        {
            "page_id": "5fbd873dc7da4ffbaf69273e",
            "site_info": site_info,
            "post1": post1,
            "post2": post2,
            "post3": post3,
            "post4": post4,
            "blog_posts": blog_posts,
            "featured_blogs": featured_blogs,
            "blog_categories": blog_categories,
        },
    )


def blog_category(request, category):
    site_info = SiteInfo.objects.last()
    post1, post2, post3, post4 = InstagramPost.objects.all()
    blog_posts = BlogPost.objects.filter(category__category=category).order_by(
        "-created_at"
    )
    featured_blogs = BlogPost.objects.filter(
        is_featured=True, category__category=category
    ).order_by("-created_at")[:3]
    blog_categories = BlogCategory.objects.all()

    return render(
        request,
        "blog.html",
        {
            "page_id": "5fbd873dc7da4ffbaf69273e",
            "site_info": site_info,
            "post1": post1,
            "post2": post2,
            "post3": post3,
            "post4": post4,
            "blog_posts": blog_posts,
            "featured_blogs": featured_blogs,
            "blog_categories": blog_categories,
        },
    )


def blog_details(request, slug):
    site_info = SiteInfo.objects.last()
    blog_post_filter = list(
        filter(
            lambda blog_post: blog_post.slug == slug,
            BlogPost.objects.all().order_by("-created_at"),
        )
    )
    blog_post = blog_post_filter[0] if len(blog_post_filter) > 0 else None
    popular_posts = BlogPost.objects.order_by("-comments__count").order_by(
        "-created_at"
    )[:3]

    if len(blog_post_filter) == 0:
        return HttpResponseNotFound("")

    if request.method == "POST":
        username = request.POST.get("username", None)
        email = request.POST.get("email", None)
        comment = request.POST.get("comment", None)

        BlogComment.objects.create(
            name=username, comment=comment, email=email, post=blog_post
        )

    return render(
        request,
        "blog-single.html",
        {
            "page_id": "",
            "site_info": site_info,
            "blog_post": blog_post,
            "popular_posts": popular_posts,
        },
    )


def contact(request):
    site_info = SiteInfo.objects.last()
    post1, post2, post3, post4 = InstagramPost.objects.all()
    success_message = None
    error_message = None

    if request.method == "POST":
        first_name = request.POST.get("first-name", None)
        last_name = request.POST.get("last-name", None)
        email = request.POST.get("email", None)
        phone_number = request.POST.get("mobile", None)
        message = request.POST.get("message", None)
        
        try:
            ContactInfo.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                message=message,
            )
            success_message = "message was submitted succesfully"
        except Exception as e:
            error_message = str(e)
            
        print(f"success_message: {success_message}")
        print(f"error_message: {error_message}")

    return render(
        request,
        "contact-us.html",
        {
            "page_id": "5fbd7f40eeaa93622d5f498c",
            "site_info": site_info,
            "success_message": success_message,
            "error_message": error_message,
            "post1": post1,
            "post2": post2,
            "post3": post3,
            "post4": post4,
        },
    )


def privacy_policy(request):
    site_info = SiteInfo.objects.last()
    return render(
        request,
        "privacy-policy.html",
        {"page_id": "5fbd873dc7da4ffbaf69273e", "site_info": site_info},
    )
