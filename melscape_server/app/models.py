from django.db import models
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField

from random import randint
class LandingHeroSection(models.Model):
    header = models.CharField(max_length=300)
    details = models.TextField(default="")
    first_button_text = models.CharField(max_length=50)
    first_button_link = models.CharField(max_length=200)
    second_button_text = models.CharField(max_length=50)
    second_button_link = models.CharField(max_length=200)
    cover_photo = models.ImageField(upload_to="landing")
    slogan_header = models.CharField(max_length=200)
    
    def __str__(self):
        return "Landing Page Hero Section"  
 
class CTADescription(models.Model):
    header = models.CharField(max_length=200)
    details_top = models.TextField(default="")
    details_bottom = models.TextField(default="")
    is_aligned_left = models.BooleanField(default=False)
    cta_button_text = models.CharField(max_length=50, default="")
    cta_button_link = models.CharField(max_length=300, default="")
    side_photo = models.ImageField(upload_to="CTA", blank=True)
    
    def __str__(self):
        return f"Call To Action: {self.header}"
 
 
class CoreService(models.Model):
    header = models.CharField(max_length=200)
    details = models.TextField()
    icon_name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Core Service: {self.header}"
 

class StepsToEarn(models.Model):
    cover_photo = models.ImageField(upload_to="earn")
    step_text = models.CharField(max_length=50)
    cta_button_link = models.CharField(max_length=200)
    
    def __str__(self):
        return f"Step To Earn: {self.step_text}" 
 
class FAQCategory(models.Model):
    category = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category

class FAQ(models.Model):
    question = models.CharField(max_length=400)
    answer = RichTextField(blank=True, null=True)
    category = models.ForeignKey(FAQCategory, on_delete=models.DO_NOTHING, related_name="faqs")
    
    def __str__(self):
        return f"FAQ: {self.question} \t| | [Category]:{self.category.category}"
    
    
class AboutHeroSection(models.Model):
    header = models.CharField(max_length=200)
    cover_photo = models.ImageField(upload_to="about")
    
    def __str__(self):
        return f"About Us Page Hero Section"
    
class AboutIntroSection(models.Model):
    detail_top = models.TextField()
    detail_bottom = models.TextField()
    
    def __str__(self):
        return f"About Us Page Intro Section"
    

def validate_svg_or_image(file):
    if not file.name.endswith(('.svg', '.png', '.jpg', '.jpeg')):
        raise ValidationError("Only SVG, PNG, JPG, and JPEG formats are supported.")
class HowWeCanHelpSection(models.Model):
    icon = models.FileField(upload_to="help", validators=[validate_svg_or_image])
    description = models.TextField()
    
    def __str__(self):
        return f"{self.description[:50]}...."
   
    
class SiteInfo(models.Model):
    facebook_link = models.CharField(max_length=300, default="")
    tiktok_link = models.CharField(max_length=300, default="")
    linkedin_link = models.CharField(max_length=300, default="")
    instagram_link = models.CharField(max_length=300, default="")
    email_1 = models.CharField(max_length=300, default="")
    email_2 = models.CharField(max_length=300, default="")
    phone_number = models.CharField(max_length=300, default="")
    calendly_link = models.CharField(max_length=300, default="")
    booking_link = models.CharField(max_length=300, default="")
    airbnb_link = models.CharField(max_length=300, default="")
    tripadvisor_link = models.CharField(max_length=300, default="")
    
    def __str__(self):
        return "Melscape Contact Info"
    
class InstagramPost(models.Model):
    post_name = models.CharField(max_length=200)
    post_link = models.CharField(max_length=300)
    post_image = models.ImageField(upload_to="instagram")
    
    def __str__(self):
        return f"Instagram Post: {self.post_name}"
   
class BlogCategory(models.Model):
    category = models.CharField(max_length=300)

    def __str__(self):
        return f"Category: {self.category}"
    
class BlogPost(models.Model):
    heading = models.CharField(max_length=500, unique=True)
    body = RichTextField(null=True, blank=True)
    cover_photo = models.ImageField(upload_to="blog", null=True, blank=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name="blog_posts")
    author = models.CharField(max_length=100, default="Admin")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Blog Post: {self.heading[:100]}"
    
    @property
    def slug(self):
        return self.heading.lower().replace(" ", "_")
    
    
class BlogComment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    comment = models.TextField()
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}'s || Comment: {self.comment[:100]} || Time: {self.created_at}"
    
class BlogImage(models.Model):
    image = models.ImageField(upload_to="blog", blank=True, null=True)
    
    def __str__(self):
        return f"Blog Image: {self.image.name}"
    
class ContactInfo(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return f"Contact: {self.first_name} {self.last_name} || Email: {self.email}"
    
    
class AppointmentBookingRequest(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Email: {self.email} || Location: {self.location} || Message: {self.message[:80]}"