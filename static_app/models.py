from django.db import models
from ckeditor.fields import RichTextField
import uuid


# Create your models here.

# Register your models here.

class Banner(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    image=models.ImageField(upload_to="banner/%Y/%m/%d/", null=True, blank=True)
    content = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

class WorkWith(models.Model):
    image=models.ImageField(upload_to="workwith/%Y/%m/%d/", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    slug = models.CharField(max_length=250, unique=True, default=uuid.uuid4)

class About(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    content = RichTextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    slug = models.CharField(max_length=250, unique=True, default=uuid.uuid4)

class CompanyStatus(models.Model):
    clients = models.CharField(max_length=250, null=True, blank=True)
    projects = models.CharField(max_length=250, null=True, blank=True)
    hours_Of_Support = models.CharField(max_length=250, null=True, blank=True)
    workers = models.CharField(max_length=250, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    slug = models.CharField(max_length=250, unique=True, default=uuid.uuid4)

class Portfolio(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to="portfolio/%Y/%m/%d/", null=True, blank=True)
    content = models.CharField(max_length=250, null=True, blank=True)
    url = models.CharField(max_length=250, null=True, blank=True)
    type = models.CharField(max_length=250, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    slug = models.CharField(max_length=250, unique=True, default=uuid.uuid4)

class Services(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    content = models.CharField(max_length=250, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    slug = models.CharField(max_length=250, unique=True, default=uuid.uuid4)

class FAQ(models.Model):
    select_type=models.CharField(max_length=250, null=True, blank=True)
    question = models.CharField(max_length=250, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    title=models.CharField(max_length=250, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    slug = models.CharField(max_length=250, unique=True, default=uuid.uuid4)

class Team(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to="team/%Y/%m/%d/", null=True, blank=True)
    designation = models.CharField(max_length=250, null=True, blank=True)
    detail = models.CharField(max_length=250, null=True, blank=True)
    twitter = models.CharField(max_length=250, null=True, blank=True)
    facebook = models.CharField(max_length=250, null=True, blank=True)
    instagram = models.CharField(max_length=250, null=True, blank=True)
    linkedin = models.CharField(max_length=250, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    slug = models.CharField(max_length=250, unique=True, default=uuid.uuid4)

class Testimonial(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    desgination = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    testimonial_image = models.ImageField(upload_to="testimonial/%Y/%m/%d/", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    slug = models.CharField(max_length=250, unique=True, default=uuid.uuid4)


class Blog(models.Model):
    blog_header= models.CharField(max_length=250, null=True, blank=True)
    blog_title = models.CharField(max_length=250, null=True, blank=True)
    blog_video = models.FileField(upload_to="Blog/", null=True, blank=True)
    blog_image = models.ImageField(upload_to="Blog/%Y/%m/%d/", null=True, blank=True)
    blog_type = models.CharField(max_length=250, null=True, blank=True)
    visitor = models.IntegerField(default=0, null=True, blank=True)
    meta_description = RichTextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    slug = models.CharField(max_length=250, unique=True, default=uuid.uuid4)

class BlogVisitor(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE, null=True, blank=True)
    visitor_user = models.CharField(max_length=250, null=True, blank=True)

class ContactUs(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)
    subject = models.CharField(max_length=250, null=True, blank=True)
    message = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)


class CustomerService(models.Model):
    tollfree1 = models.CharField(max_length=250, null=True, blank=True) 
    tollfree2 = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(unique=False)
    address = models.CharField(max_length=250, null=True, blank=True)
    servicehours = models.TextField(null=True,blank=True)
    iphonelink = models.CharField(max_length=250, null=True, blank=True)
    androidlink = models.CharField(max_length=250, null=True, blank=True)  
    created_at = models.DateField(auto_now_add=True)
    slug = models.CharField(max_length=250, unique=True, default=uuid.uuid4) 


class GlobalSetting(models.Model):
    text = models.TextField(null=True, blank=True)
    global_image = models.ImageField(
        upload_to="globalsetting/%Y/%m/%d/", null=True, blank=True
    )
    logo_image = models.ImageField(
        upload_to="globalsetting/%Y/%m/%d/", null=True, blank=True
    )
    global_url_insta = models.URLField(null=True, blank=True)
    global_url_facebook = models.URLField(null=True, blank=True)
    global_url_twitter = models.URLField(null=True, blank=True)
    insta_is_active = models.BooleanField(default=True)
    facebook_is_active = models.BooleanField(default=True)
    twitter_is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    slug = models.CharField(max_length=250, unique=True, default=uuid.uuid4)


class Heading(models.Model):
    services = models.TextField(max_length=250, null=True, blank=True) 
    portfolio = models.TextField(max_length=250, null=True, blank=True) 
    faq = models.TextField(max_length=250, null=True, blank=True) 
    team = models.TextField(max_length=250, null=True, blank=True) 
    call_to_action = models.TextField(max_length=250, null=True, blank=True) 
    testimonials = models.TextField(max_length=250, null=True, blank=True) 
    recent_posts = models.TextField(max_length=250, null=True, blank=True) 
    contact = models.TextField(max_length=250, null=True, blank=True) 


