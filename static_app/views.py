from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages


# Create your views here.
def Home(request):
    template_name="web/home.html"
    globlesetting=GlobalSetting.objects.get(id=1)
    banner=Banner.objects.get(id=1)
    about=About.objects.all()
    about1=about.get(id=1)
    company_status=CompanyStatus.objects.get(id=1)
    services=Services.objects.all()
    portfolio=Portfolio.objects.all()
    faq=FAQ.objects.all()
    teams=Team.objects.all()
    testimonial=Testimonial.objects.all()
    costomer_service=CustomerService.objects.get(id=1)
    blog=Blog.objects.all()
    heading=Heading.objects.get(id=1)
    clients=Clients.objects.all()
    return render(request, template_name,{'banner':banner, 'about':about, 'about1':about1, 'company_status':company_status, 'services':services, 'portfolio':portfolio, 'faq':faq, 'teams':teams,'testimonial':testimonial,'costomer_service':costomer_service,'blog':blog,'heading':heading,'clients':clients,'globlesetting':globlesetting})


def BlogDetail(request,slug):
    template_name="web/blog-details.html"
    globlesetting=GlobalSetting.objects.get(id=1)
    costomer_service=CustomerService.objects.get(id=1)
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META.get('HTTP_X_FORWARDED_FOR').split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    heading=Heading.objects.get(id=1)
    blog=Blog.objects.get(slug=slug)
    if not BlogVisitor.objects.filter(blog_id=blog.id,visitor_user=ip):
        blog.visitor+=1
        blog.save()
        BlogVisitor.objects.create(blog_id=blog.id,visitor_user=ip)

    return render(request, template_name,{'blog':blog,'costomer_service':costomer_service,'heading':heading,'globlesetting':globlesetting})

def BlogList(request):
    template_name="web/blog.html"
    globlesetting=GlobalSetting.objects.get(id=1)
    costomer_service=CustomerService.objects.get(id=1)
    heading=Heading.objects.get(id=1)
    blog=Blog.objects.all()
    return render(request, template_name,{'blog':blog,'costomer_service':costomer_service,'heading':heading,'globlesetting':globlesetting})

                     
def PortfolioDetail(request):
    template_name="web/portfolio-details.html"
    globlesetting=GlobalSetting.objects.get(id=1)
    costomer_service=CustomerService.objects.get(id=1)
    return render(request, template_name,{'costomer_service':costomer_service,'globlesetting':globlesetting})


def ServicesDetail(request):
    template_name="web/services-details.html"
    globlesetting=GlobalSetting.objects.get(id=1)
    costomer_service=CustomerService.objects.get(id=1)
    return render(request, template_name,{'costomer_service':costomer_service,'globlesetting':globlesetting})


def AboutUs(request):
    template_name="web/about-us.html"
    globlesetting=GlobalSetting.objects.get(id=1)
    costomer_service=CustomerService.objects.get(id=1)
    about=About.objects.get(id=1)
    return render(request, template_name,{"about":about,'costomer_service':costomer_service,'globlesetting':globlesetting})


def ContactUS(request):
    template_name="web/contact-us.html"
    globlesetting=GlobalSetting.objects.get(id=1)
    heading=Heading.objects.get(id=1)
    costomer_service=CustomerService.objects.get(id=1)
    if request.POST:
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact_uS=ContactUs.objects.create(name=name,email=email,subject=subject,message=message)
        if not email:
            messages.error(request,"email requried")
        messages.success(request,'Mail sent successfully !!')
        return redirect(request.META['HTTP_REFERER'])
    return render(request, template_name,{'costomer_service':costomer_service,'heading':heading,'globlesetting':globlesetting})


def GivaHome(request):
    template_name="web/giva_home.html"
    return render(request, template_name)
    
def ServicesList(request):
    template_name="web/service-list.html"
    globlesetting=GlobalSetting.objects.get(id=1)
    banner=Banner.objects.get(id=1)
    about=About.objects.all()
    about1=about.get(id=1)
    company_status=CompanyStatus.objects.get(id=1)
    services=Services.objects.all()
    portfolio=Portfolio.objects.all()
    faq=FAQ.objects.all()
    teams=Team.objects.all()
    testimonial=Testimonial.objects.all()
    costomer_service=CustomerService.objects.get(id=1)
    blog=Blog.objects.all()
    heading=Heading.objects.get(id=1)
    clients=Clients.objects.all()
    return render(request, template_name,{'banner':banner, 'about':about, 'about1':about1, 'company_status':company_status, 'services':services, 'portfolio':portfolio, 'faq':faq, 'teams':teams,'testimonial':testimonial,'costomer_service':costomer_service,'blog':blog,'heading':heading,'clients':clients,'globlesetting':globlesetting})

