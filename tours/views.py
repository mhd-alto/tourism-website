from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import Tour,TourImg
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from cart.models import Cart,CartItem
from django.db.models import Q
from django.contrib.auth.decorators import login_required



def tourDetails(request,tour_id,title):
    package = get_object_or_404(Tour,pk=tour_id)
    package_imgs = TourImg.objects.filter(tour=package)
    return render(request,'toursDetails.html',{"package":package,"package_imgs":package_imgs})

def tourItemCart(request,tour_id,title):
    package = get_object_or_404(Tour,pk=tour_id)
    package_imgs = TourImg.objects.filter(tour=package)
    return render(request,'toursDetails.html',{"package":package,"package_imgs":package_imgs})

def tourItemCartAr(request,tour_id,title):
    package = get_object_or_404(Tour,pk=tour_id)
    package_imgs = TourImg.objects.filter(tour=package)
    return render(request,'toursDetailsAr.html',{"package":package,"package_imgs":package_imgs})

def tourList(request):
    packages = Tour.objects.all().order_by('-created')
    imgs = TourImg.objects.all()
    last_package = Tour.objects.last()
    first_img = Tour.objects.first()
    last_img = Tour.objects.last()
    a = Paginator(packages,5)
    page_number = request.GET.get('page')
    try:
        page_obj = a.get_page(page_number)
    except PageNotAnInteger:
        page_obj = a.page(1)
    except EmptyPage:
        page_obj = a.page(a.num_pages)
    context = {"packages":page_obj,"imgs":imgs,"last_package":last_package,"first_img":first_img,"last_img":last_img}
    return render(request,'tourList.html',context)


def tourDetailsAr(request,tour_id,title):
    package = get_object_or_404(Tour,pk=tour_id)
    package_imgs = TourImg.objects.filter(tour=package)
    return render(request,'toursDetailsAr.html',{"package":package,"package_imgs":package_imgs})

def tourListAr(request):
    packages = Tour.objects.all().order_by('-created')
    imgs = TourImg.objects.all()
    last_package = Tour.objects.last()
    first_img = Tour.objects.first()
    last_img = Tour.objects.last()
    a = Paginator(packages,5)
    page_number = request.GET.get('page')
    try:
        page_obj = a.get_page(page_number)
    except PageNotAnInteger:
        page_obj = a.page(1)
    except EmptyPage:
        page_obj = a.page(a.num_pages)
    context = {"packages":page_obj,"imgs":imgs,"last_package":last_package,"first_img":first_img,"last_img":last_img}
    return render(request,'tourListAr.html',context)


@login_required(login_url='login')
def addToCart(request,tour_id):
    tour = get_object_or_404(Tour,pk=tour_id)
    try:
        cart = Cart.objects.get(added_by=request.user,is_active=False)
        cartItems = CartItem.objects.filter(cart=cart)
        item = CartItem(content_object=tour,object_id=tour.id,cart=cart)
        item.title = item.content_object.title
        item.titleAr = item.content_object.titleAr
        for i in cartItems:
            if i.content_object == item.content_object:
                i.count += 1
                i.save()
                print(i.count)
                return redirect("tourList")
        try:
            item.save()
            return redirect('tourList')
        except:
            return HttpResponse('opps!! item not added') 
    except:
        print('_________________________________________')
        cart = Cart(added_by=request.user,is_active=False)
        cart.save()
        cart = Cart.objects.get(added_by=request.user,is_active=False)
        cartItems = CartItem.objects.filter(cart=cart)
        if cart:
            item = CartItem(content_object=tour,object_id=tour.id,cart=cart)
            item.title = item.content_object.title
            item.titleAr = item.content_object.titleAr
            for i in cartItems:
                if i.content_object.id == item.content_object.id:
                    i.count += 1
                    i.save()
                    print(i.count)
                    return redirect("tourList")
            try:
                item.save()
                return redirect('tourList')
            except:
                return HttpResponse('opps!! item not added')
    

def searchTour(request):
    search_tour = request.POST.get('search')
    if request.method == "POST":

        if (Tour.objects.filter(Q(title__icontains = search_tour) | 
        Q(titleAr__icontains = search_tour))):
            print(1)
            tours = Tour.objects.filter(Q(title__icontains = search_tour) | 
            Q(titleAr__icontains = search_tour))
            tours = tours.order_by("-updated") 

        elif(Tour.objects.filter(Q(tourProgram__icontains = search_tour) | 
        Q(tourProgramAr__icontains = search_tour))):
            print(2)
            tours = Tour.objects.filter(Q(tourProgram__icontains = search_tour) | 
            Q(tourProgramAr__icontains = search_tour))
            tours = tours.order_by("-updated")
        else:
            tours = Tour.objects.none()
            print(3)

        last_package = Tour.objects.last()
        a = Paginator(tours,10)
        page_number = request.GET.get('page')
        try:
            page_obj = a.get_page(page_number)
        except PageNotAnInteger:
            page_obj = a.page(1)
        except EmptyPage:
            page_obj = a.page(a.num_pages)
    context = {'packages':page_obj,"last_package":last_package}
    return render(request,'tourList.html',context)


def searchTourAr(request):
    search_tour = request.POST.get('search')
    if request.method == "POST":

        if (Tour.objects.filter(Q(title__icontains = search_tour) | 
        Q(titleAr__icontains = search_tour))):
            print(1)
            tours = Tour.objects.filter(Q(title__icontains = search_tour) | 
            Q(titleAr__icontains = search_tour))
            tours = tours.order_by("-updated") 

        elif(Tour.objects.filter(Q(tourProgram__icontains = search_tour) | 
        Q(tourProgramAr__icontains = search_tour))):
            print(2)
            tours = Tour.objects.filter(Q(tourProgram__icontains = search_tour) | 
            Q(tourProgramAr__icontains = search_tour))
            tours = tours.order_by("-updated")
        else:
            tours = Tour.objects.none()
            print(3)
        last_package = Tour.objects.last()
        
        a = Paginator(tours,10)
        page_number = request.GET.get('page')
        try:
            page_obj = a.get_page(page_number)
        except PageNotAnInteger:
            page_obj = a.page(1)
        except EmptyPage:
            page_obj = a.page(a.num_pages)
    context = {'packages':page_obj,"last_package":last_package}
    return render(request,'tourListAr.html',context)
