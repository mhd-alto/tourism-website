from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import Package,PackageImg
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from cart.models import Cart,CartItem
from django.db.models import Q
from django.contrib.auth.decorators import login_required



def packageDetails(request,package_id,title):
    package = get_object_or_404(Package,pk=package_id)
    package_imgs = PackageImg.objects.filter(Package=package)
    return render(request,'packageDetails.html',{"package":package,"package_imgs":package_imgs})

def packageDetailsAr(request,package_id,title):
    package = get_object_or_404(Package,pk=package_id)
    package_imgs = PackageImg.objects.filter(Package=package)
    return render(request,'packageDetailsAr.html',{"package":package,"package_imgs":package_imgs})

def packageItemCart(request,package_id,title):
    package = get_object_or_404(Package,pk=package_id)
    package_imgs = PackageImg.objects.filter(Package=package)
    return render(request,'packageDetails.html',{"package":package,"package_imgs":package_imgs})

def packageItemCartAr(request,package_id,title):
    package = get_object_or_404(Package,pk=package_id)
    package_imgs = PackageImg.objects.filter(Package=package)
    return render(request,'packageDetailsAr.html',{"package":package,"package_imgs":package_imgs})

def packageList(request):
    packages = Package.objects.all().order_by('-created')
    imgs = PackageImg.objects.all()
    last_package = Package.objects.last()
    first_img = PackageImg.objects.first()
    last_img = PackageImg.objects.last()
    a = Paginator(packages,5)
    page_number = request.GET.get('page')
    try:
        page_obj = a.get_page(page_number)
    except PageNotAnInteger:
        page_obj = a.page(1)
    except EmptyPage:
        page_obj = a.page(a.num_pages)
    context = {"packages":page_obj,"imgs":imgs,"last_package":last_package,"first_img":first_img,"last_img":last_img}
    return render(request,'packageList.html',context)

def packageListAr(request):
    packages = Package.objects.all().order_by('-created')
    imgs = PackageImg.objects.all()
    last_package = Package.objects.last()
    first_img = PackageImg.objects.first()
    last_img = PackageImg.objects.last()
    a = Paginator(packages,5)
    page_number = request.GET.get('page')
    try:
        page_obj = a.get_page(page_number)
    except PageNotAnInteger:
        page_obj = a.page(1)
    except EmptyPage:
        page_obj = a.page(a.num_pages)
    context = {"packages":page_obj,"imgs":imgs,"last_package":last_package,"first_img":first_img,"last_img":last_img}
    return render(request,'packageListAr.html',context)


@login_required(login_url='login')
def addToCart(request,package_id):
    package = get_object_or_404(Package,pk=package_id)
    try:
        cart = Cart.objects.get(added_by=request.user,is_active=False)
        cartItems = CartItem.objects.filter(cart=cart)
        item = CartItem(content_object=package,object_id=package.id,cart=cart)
        item.title = item.content_object.title
        item.titleAr = item.content_object.titleAr
        for i in cartItems:
            if i.content_object == item.content_object:
                i.count += 1
                i.save()
                print(i.count)
                return redirect("packageList")
        try:
            item.save()
            return redirect('packageList')
        except:
            return HttpResponse('opps!! item not added') 
    except:
        print('_________________________________________')
        cart = Cart(added_by=request.user,is_active=False)
        cart.save()
        cart = Cart.objects.get(added_by=request.user,is_active=False)
        cartItems = CartItem.objects.filter(cart=cart)
        if cart:
            item = CartItem(content_object=package,object_id=package.id,cart=cart)
            item.title = item.content_object.title
            item.titleAr = item.content_object.titleAr
            for i in cartItems:
                if i.content_object.id == item.content_object.id:
                    i.count += 1
                    i.save()
                    print(i.count)
                    return redirect("packageList")
            try:
                item.save()
                return redirect('packageList')
            except:
                return HttpResponse('opps!! item not added')



def searchPackage(request):
    search_package = request.POST.get('search')
    if request.method == "POST":
        if (Package.objects.filter(Q(title__icontains = search_package) |
        Q(titleAr__icontains = search_package))):
            print(1)
            packages = Package.objects.filter(Q(title__icontains = search_package) |
            Q(titleAr__icontains = search_package))
            packages = packages.order_by("-updated") 

        elif(Package.objects.filter(Q(packageProgram__icontains = search_package) |
        Q(packageProgramAr__icontains = search_package))):
            packages = Package.objects.filter(Q(packageProgram__icontains = search_package) |
            Q(packageProgramAr__icontains = search_package))
            packages = packages.order_by("-updated")
        else:
            packages = Package.objects.none()


        last_package = Package.objects.last()
        a = Paginator(packages,10)
        page_number = request.GET.get('page')
        try:
            page_obj = a.get_page(page_number)
        except PageNotAnInteger:
            page_obj = a.page(1)
        except EmptyPage:
            page_obj = a.page(a.num_pages)
    context = {'packages':page_obj,"last_package":last_package}
    return render(request,'packageList.html',context)

def searchPackageAr(request):
    search_package = request.POST.get('search')
    if request.method == "POST":
        if (Package.objects.filter(Q(title__icontains = search_package) |
        Q(titleAr__icontains = search_package))):
            print(1)
            packages = Package.objects.filter(Q(title__icontains = search_package) |
            Q(titleAr__icontains = search_package))
            packages = packages.order_by("-updated") 

        elif(Package.objects.filter(Q(packageProgram__icontains = search_package) |
        Q(packageProgramAr__icontains = search_package))):
            packages = Package.objects.filter(Q(packageProgram__icontains = search_package) |
            Q(packageProgramAr__icontains = search_package))
            packages = packages.order_by("-updated")
        else:
            packages = Package.objects.none()


        last_package = Package.objects.last()
        a = Paginator(packages,10)
        page_number = request.GET.get('page')
        try:
            page_obj = a.get_page(page_number)
        except PageNotAnInteger:
            page_obj = a.page(1)
        except EmptyPage:
            page_obj = a.page(a.num_pages)
    context = {'packages':page_obj,"last_package":last_package}
    return render(request,'packageListAr.html',context)
