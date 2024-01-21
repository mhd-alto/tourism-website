from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import Visa
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from cart.models import Cart,CartItem
from django.contrib.auth.decorators import login_required
from django.db.models import Q



def searchVisa(request):
    search_visa = request.POST.get('search')
    if request.method == "POST":
        if (Visa.objects.filter(Q(title__icontains = search_visa) | 
        Q(titleAr__icontains = search_visa))):
            print(1)
            visa = Visa.objects.filter(Q(title__icontains = search_visa) | 
            Q(titleAr__icontains = search_visa))
            visa = visa.order_by("-updated") 

        elif(Visa.objects.filter(Q(description__icontains = search_visa) | 
        Q(descriptionAr__icontains = search_visa))):
            print(2)
            visa = Visa.objects.filter(Q(description__icontains = search_visa) | 
            Q(descriptionAr__icontains = search_visa))
            visa = visa.order_by("-updated")
        else:
            visa = Visa.objects.none()
            print(3)
        Last_visa = Visa.objects.last()
        a = Paginator(visa,10)
        page_number = request.GET.get('page')
        try:
            page_obj = a.get_page(page_number)
        except PageNotAnInteger:
            page_obj = a.page(1)
        except EmptyPage:
            page_obj = a.page(a.num_pages)
    context = {'packages':page_obj,"Last_visa":Last_visa}
    return render(request,'visaList.html',context)


def searchVisaAr(request):
    search_visa = request.POST.get('search')
    if request.method == "POST":
        if (Visa.objects.filter(Q(title__icontains = search_visa) | 
        Q(titleAr__icontains = search_visa))):
            print(1)
            visa = Visa.objects.filter(Q(title__icontains = search_visa) | 
            Q(titleAr__icontains = search_visa))
            visa = visa.order_by("-updated") 

        elif(Visa.objects.filter(Q(description__icontains = search_visa) | 
        Q(descriptionAr__icontains = search_visa))):
            print(2)
            visa = Visa.objects.filter(Q(description__icontains = search_visa) | 
            Q(descriptionAr__icontains = search_visa))
            visa = visa.order_by("-updated")
        else:
            visa = Visa.objects.none()
            print(3)
        Last_visa = Visa.objects.last()
        a = Paginator(visa,10)
        page_number = request.GET.get('page')
        try:
            page_obj = a.get_page(page_number)
        except PageNotAnInteger:
            page_obj = a.page(1)
        except EmptyPage:
            page_obj = a.page(a.num_pages)
    context = {'packages':page_obj,"Last_visa":Last_visa}
    return render(request,'visaListAr.html',context)


def visaList(request):
    visa = Visa.objects.all().order_by('-updated')
    Last_visa = Visa.objects.last()
    a = Paginator(visa,5)
    page_number = request.GET.get('page')
    try:
        page_obj = a.get_page(page_number)
    except PageNotAnInteger:
        page_obj = a.page(1)
    except EmptyPage:
        page_obj = a.page(a.num_pages)
    context = {"packages":page_obj,"Last_visa":Last_visa}
    return render(request,'visaList.html',context)

def visaListAr(request):
    visa = Visa.objects.all().order_by('-updated')
    Last_visa = Visa.objects.last()
    a = Paginator(visa,5)
    page_number = request.GET.get('page')
    try:
        page_obj = a.get_page(page_number)
    except PageNotAnInteger:
        page_obj = a.page(1)
    except EmptyPage:
        page_obj = a.page(a.num_pages)
    context = {"packages":page_obj,"Last_visa":Last_visa}
    return render(request,'visaListAr.html',context)


@login_required(login_url='login')
def addToCart(request,visa_id):
    visa = get_object_or_404(Visa,pk=visa_id)
    try:
        cart = Cart.objects.get(added_by=request.user,is_active=False)
        cartItems = CartItem.objects.filter(cart=cart)
        item = CartItem(content_object=visa,object_id=visa.id,cart=cart)
        item.title = item.content_object.title
        item.titleAr = item.content_object.titleAr
        for i in cartItems:
            if i.content_object == item.content_object:
                i.count += 1
                i.save()
                print(i.count)
                return redirect("visas")
        try:
            item.save()
            return redirect('visas')
        except:
            return HttpResponse('opps!! item not added') 
    except:
        print('_________________________________________')
        cart = Cart(added_by=request.user,is_active=False)
        cart.save()
        cart = Cart.objects.get(added_by=request.user,is_active=False)
        cartItems = CartItem.objects.filter(cart=cart)
        if cart:
            item = CartItem(content_object=visa,object_id=visa.id,cart=cart)
            item.title = item.content_object.title
            item.titleAr = item.content_object.titleAr
            for i in cartItems:

                if i.content_object == item.content_object:
                    i.count += 1
                    i.save()
                    print(i.count)
                    return redirect("visas")
            try:
                item.save()
                return redirect('visas')
            except:
                return HttpResponse('opps!! item not added')

def visaDetails(request,visa_id):
    visa = get_object_or_404(Visa,pk=visa_id)
    return render(request,'visaDetails.html',{"visa":visa})

def visaDetailsAr(request,visa_id):
    visa = get_object_or_404(Visa,pk=visa_id)
    return render(request,'visaDetailsAr.html',{"visa":visa})


        
               
