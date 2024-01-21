from django.shortcuts import render,get_object_or_404,redirect
from packages.models import Package
from account.models import Slider,Blog,WhyUs,FAQ,FAQAR
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Message
from .forms import MessageForm,MessageFormAr
from django.db.models import Q
from taggit.models import Tag


def index(request):
    incorrect = False
    if request.method == "POST":
        form = MessageForm(request.POST)
        username = request.GET.get('user_name')
        email = request.GET.get('email')
        phonenumber = request.GET.get('phoneNumber')
        subject = request.GET.get('subject')
        message = request.GET.get('message')
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            incorrect = True
            form = MessageForm(request.POST)
            form.user_name = username
            form.email = email
            form.subject = subject
            form.phoneNumber = phonenumber
            form.message = message
            packages = Package.objects.all().order_by('-created')[:5]
            fs = Slider.objects.first()
            slider = Slider.objects.all()[1:]
            slider_img = Slider.objects.all()
            blogs = Blog.objects.all().order_by('-id')[:9]
            whyUs = WhyUs.objects.first()
            faq = FAQ.objects.first()
            context = {"packages":packages,"slider":slider,"fs":fs,"slider_img":slider_img,"blogs":blogs,
            'whyUs':whyUs,'faq':faq,'incorrect':incorrect,"form":form}
            return render(request,'index.htm',context)
    else:
        form = MessageForm()
        packages = Package.objects.all().order_by('-created')[:5]
        fs = Slider.objects.first()
        slider = Slider.objects.all()[1:]
        slider_img = Slider.objects.all()
        blogs = Blog.objects.all().order_by('-id')[:9]
        whyUs = WhyUs.objects.first()
        faq = FAQ.objects.first()
        context = {"packages":packages,"slider":slider,"fs":fs,"slider_img":slider_img,"blogs":blogs
        ,'whyUs':whyUs,'faq':faq,'incorrect':incorrect,"form":form}
    return render(request,'index.htm',context)



def indexAr(request):
    incorrect = False
    if request.method == "POST":
        form = MessageFormAr(request.POST)
        username = request.GET.get('user_name')
        email = request.GET.get('email')
        subject = request.GET.get('subject')
        message = request.GET.get('message')
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            incorrect = True
            form = MessageFormAr(request.POST)
            form.user_name = username
            form.email = email
            form.subject = subject
            form.message = message
            packages = Package.objects.all().order_by('-created')[:5]
            fs = Slider.objects.first()
            slider = Slider.objects.all()[1:]
            slider_img = Slider.objects.all()
            blogs = Blog.objects.all().order_by('-id')[:9]
            whyUs = WhyUs.objects.first()
            faq = FAQAR.objects.first()
            context = {"packages":packages,"slider":slider,"fs":fs,"slider_img":slider_img,"blogs":blogs,
            'whyUs':whyUs,'faq':faq,'incorrect':incorrect,"form":form}
            return render(request,'indexar.html',context)
    else:
        form = MessageFormAr()
        packages = Package.objects.all().order_by('-created')[:5]
        fs = Slider.objects.first()
        slider = Slider.objects.all()[1:]
        slider_img = Slider.objects.all()
        blogs = Blog.objects.all().order_by('-id')[:9]
        whyUs = WhyUs.objects.first()
        faq = FAQAR.objects.first()
    context = {"packages":packages,"slider":slider,"fs":fs,"slider_img":slider_img,"blogs":blogs
    ,'whyUs':whyUs,'faq':faq,'incorrect':incorrect,"form":form}
    return render(request,'indexar.html',context)


def blogs(request):
    blog = Blog.objects.all().order_by('-id')
    a = Paginator(blog,10)
    page_number = request.GET.get('page')
    try:
        page_obj = a.get_page(page_number)
    except PageNotAnInteger:
        page_obj = a.page(1)
    except EmptyPage:
        page_obj = a.page(a.num_pages)
    context = {'blogs':page_obj}
    return render(request,'blog\\blogs.html',context)

def blogsAr(request):
    blog = Blog.objects.all().order_by('-id')
    a = Paginator(blog,10)
    page_number = request.GET.get('page')
    try:
        page_obj = a.get_page(page_number)
    except PageNotAnInteger:
        page_obj = a.page(1)
    except EmptyPage:
        page_obj = a.page(a.num_pages)
    context = {'blogs':page_obj}
    return render(request,'blog\\blogsAr.html',context)


def blogDetailsAr(request,blog_id,slug):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog\\blog_detailsAr.html',{'blog':blog})

def blogDetails(request,blog_id,slug):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog\\blog_details.html',{'blog':blog})


def searchBlog(request):
    search_blog = request.POST.get('search')
    if request.method == "POST":
        if(Blog.objects.filter(tags__name__in=search_blog)):
            blog = Blog.objects.filter(tags__name__in=search_blog)

        if (Blog.objects.filter(Q(title__icontains = search_blog) |
        Q(titleAr__icontains = search_blog))):
            print(1)
            blog = Blog.objects.filter(Q(title__icontains = search_blog) | 
            Q(titleAr__icontains = search_blog))
            blog = blog.order_by("-updated") 
            print(f'{blog}___________________________-')

        elif(Blog.objects.filter(Q(description__icontains = search_blog) | 
        Q(descriptionAr__icontains = search_blog))):
            print(2)
            blog = Blog.objects.filter(Q(description__icontains = search_blog) | 
            Q(descriptionAr__icontains = search_blog))
            blog = blog.order_by("-updated")
        else:
            blog = Blog.objects.none()
            print(3)
        print(f"{blog}____________________________---")
        a = Paginator(blog,10)
        page_number = request.GET.get('page')
        try:
            page_obj = a.get_page(page_number)
        except PageNotAnInteger:
            page_obj = a.page(1)
        except EmptyPage:
            page_obj = a.page(a.num_pages)
    context = {'blogs':page_obj}
    return render(request,'blog\\blogs',context)

def searchBlogAr(request):
    search_blog = request.POST.get('search')
    if request.method == "POST":
        if (Blog.objects.filter(Q(title__icontains = search_blog) |
        Q(titleAr__icontains = search_blog))):
            print(1)
            blog = Blog.objects.filter(Q(title__icontains = search_blog) | 
            Q(titleAr__icontains = search_blog))
            blog = blog.order_by("-updated") 
            print(f'{blog}___________________________-')

        elif(Blog.objects.filter(Q(description__icontains = search_blog) | 
        Q(descriptionAr__icontains = search_blog))):
            print(2)
            blog = Blog.objects.filter(Q(description__icontains = search_blog) | 
            Q(descriptionAr__icontains = search_blog))
            blog = blog.order_by("-updated")
        else:
            blog = Blog.objects.none()
            print(3)
        print(f"{blog}____________________________---")
        a = Paginator(blog,10)
        page_number = request.GET.get('page')
        try:
            page_obj = a.get_page(page_number)
        except PageNotAnInteger:
            page_obj = a.page(1)
        except EmptyPage:
            page_obj = a.page(a.num_pages)
    context = {'blogs':page_obj}
    return render(request,'blog\\blogsAr.html',context)



