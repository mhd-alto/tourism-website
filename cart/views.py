from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import Cart,CartItem
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.contenttypes.models import ContentType


def cartList(request):
    carts = Cart.objects.filter(added_by=request.user).order_by('-created')
    a = Paginator(carts,5)
    page_number = request.GET.get('page')
    try:
        page_obj = a.get_page(page_number)
    except PageNotAnInteger:
        page_obj = a.page(1)
    except EmptyPage:
        page_obj = a.page(a.num_pages)
    context = {"Carts":page_obj}
    return render(request,'CartList.html',context)

def cartListAr(request):
    carts = Cart.objects.filter(added_by=request.user).order_by('-created')
    a = Paginator(carts,5)
    page_number = request.GET.get('page')
    try:
        page_obj = a.get_page(page_number)
    except PageNotAnInteger:
        page_obj = a.page(1)
    except EmptyPage:
        page_obj = a.page(a.num_pages)
    context = {"Carts":page_obj}
    return render(request,'CartListAr.html',context)

def cartDetails(request,cart_id):
    cart = get_object_or_404(Cart,pk=cart_id)
    items = CartItem.objects.filter(cart=cart)
    items = items.order_by("-id")
    context = {"cart":cart,"items":items}
    return render(request,'cartDetails.html',context)

def cartDetailsAr(request,cart_id):
    cart = get_object_or_404(Cart,pk=cart_id)
    items = CartItem.objects.filter(cart=cart)
    items = items.order_by("-id")
    context = {"cart":cart,"items":items}
    return render(request,'cartDetailsAr.html',context)

def createCart(user):
    cart = Cart()
    cart.added_by = user
    cart.is_active = False
    cart.save()
    print('saved')
    


def deleteItem(request,item_id,cart_id):
    item = get_object_or_404(CartItem,pk=item_id)
    if(item.delete()):
        print('deleted')
    return redirect('CartDetails',cart_id)

def add(request,item_id,cart_id):
    item = get_object_or_404(CartItem,pk=item_id)
    item.count+=1
    item.save()
    return redirect('CartDetails',cart_id)

def mins(request,item_id,cart_id):
    item = get_object_or_404(CartItem,pk=item_id)
    try:
        item.count-=1
        item.save() 
        return redirect("CartDetails",cart_id)
    except:
        return redirect("CartDetails",cart_id)
        
def deactiveCart(request,cart_id):
    cart = get_object_or_404(Cart,pk=cart_id)
    cart.is_active = True
    print(f"{cart.is_active}_{cart.id}_____________________________________________")
    cart.save()
    return redirect('profile')


# def addItem(request,obj_id,type):
#     cart = Cart.objects.filter(added_by=request.user,is_active=False)
#     if request.method == "POST":
#         if cart:

#             item = CartItem(content_object=obj,object_id=o,cart=cart)
#             item.save()
#             print(item.content_object)
#             return HttpResponse("done")
#     return HttpResponse("opps!!")

        

        
        
    
            
        





