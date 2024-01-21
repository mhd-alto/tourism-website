from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render
from .models import Insurance
from cart.models import Cart,CartItem
from django.contrib.auth.decorators import login_required



def  Insurances(request):
    insurances = Insurance.objects.all()
    sinsurances = Insurance.objects.none
    fage = []
    tage = []
    pe = []
    
    for f in insurances:
        fa = f.from_age
        fage.append(fa)
        ta = f.to_age
        tage.append(ta)
        p = f.period
        pe.append(p)

    fage = [*set(fage)]
    tage = [*set(tage)]
    pe = [*set(pe)]

    if request.method == "POST":
        ageFrom = request.POST.get('from')
        ageTo = request.POST.get('to')
        Period = request.POST.get('period')
        if (ageFrom and ageTo and Period)!="-1":
            sinsurances = Insurance.objects.filter(from_age=ageFrom,to_age=ageTo)
            sinsurances = sinsurances.filter(period=Period)
            print("1")
        if ageFrom != "-1" and ageTo != "-1" and Period =="-1" :
            sinsurances = Insurance.objects.filter(from_age=ageFrom,to_age=ageTo)
            print("2")
        if ageFrom != "-1" and Period !="-1":
            sinsurances = Insurance.objects.filter(from_age=ageFrom)
            sinsurances = sinsurances.filter(period=Period)
            print('hi')
        if ageTo !="-1" and Period !="-1":
            sinsurances = Insurance.objects.filter(to_age=ageTo)
            sinsurances = sinsurances.filter(period=Period)
            print('bay')
        if ageFrom != "-1" and ageTo =="-1" and Period == "-1":
            sinsurances = Insurance.objects.filter(from_age=ageFrom)
            print("ageFrom")
        if ageTo != "-1" and ageFrom == "-1" and Period == "-1":
            sinsurances = Insurance.objects.filter(to_age=ageTo)
            print("drop")

        print(f'F{ageFrom}___T{ageTo}____P{Period}')
        
    context = {"insurances":insurances,"sinsurances":sinsurances,"f":fage,"t":tage,"p":pe}
    return render(request,'insurances.html',context)

def  InsurancesAr(request):
    insurances = Insurance.objects.all()
    sinsurances = Insurance.objects.none
    fageA = []
    tageA = []
    peA = []

    for f in insurances:
        faa = f.from_ageAr
        fageA.append(faa)
        taa = f.to_ageAr
        tageA.append(taa)
        pa = f.periodAr
        peA.append(pa)

    fageA = [*set(fageA)]
    tageA = [*set(tageA)]
    peA = [*set(peA)]
    

    if request.method == "POST":
        ageFrom = request.POST.get('from')
        ageTo = request.POST.get('to')
        Period = request.POST.get('period')
        if (ageFrom and ageTo and Period)!="-1":
            sinsurances = Insurance.objects.filter(from_ageAr=ageFrom,to_ageAr=ageTo)
            sinsurances = sinsurances.filter(periodAr=Period)
            print("1")
        if ageFrom != "-1" and ageTo != "-1" and Period =="-1" :
            sinsurances = Insurance.objects.filter(from_ageAr=ageFrom,to_ageAr=ageTo)
            print("2")
        if ageFrom != "-1" and Period !="-1":
            sinsurances = Insurance.objects.filter(from_ageAr=ageFrom)
            sinsurances = sinsurances.filter(periodAr=Period)
            print('hi')
        if ageTo !="-1" and Period !="-1":
            sinsurances = Insurance.objects.filter(to_ageAr=ageTo)
            sinsurances = sinsurances.filter(periodAr=Period)
            print('bay')
        if ageFrom != "-1" and ageTo =="-1" and Period == "-1":
            sinsurances = Insurance.objects.filter(from_ageAr=ageFrom)
            print("ageFrom")
        if ageTo != "-1" and ageFrom == "-1" and Period == "-1":
            sinsurances = Insurance.objects.filter(to_ageAr=ageTo)
            print("drop")

        print(f'F{ageFrom}___T{ageTo}____P{Period}')
        
    context = {"insurances":insurances,"sinsurances":sinsurances,
    "fa":fageA,"ta":tageA,"pa":peA}
    return render(request,'insurancesAr.html',context)


@login_required(login_url='login')
def addToCart(request,insurance_id):
    insurance = get_object_or_404(Insurance,pk=insurance_id)
    try:
        cart = Cart.objects.get(added_by=request.user,is_active=False)
        cartItems = CartItem.objects.filter(cart=cart)
        item = CartItem(content_object=insurance,object_id=insurance.id,cart=cart)
        item.title = item.content_object
        item.titleAr = item.content_object.from_ageAr
        for i in cartItems:
            if i.content_object == item.content_object:
                i.count += 1
                i.save()
                print(i.count)
                return redirect("insurances")
        try:
            item.save()
            return redirect('insurances')
        except:
            return HttpResponse('opps!! item not added') 
    except:
        print('_________________________________________')
        cart = Cart(added_by=request.user,is_active=False)
        cart.save()
        cart = Cart.objects.get(added_by=request.user,is_active=False)
        cartItems = CartItem.objects.filter(cart=cart)
        if cart:
            item = CartItem(content_object=insurance,object_id=insurance.id,cart=cart)
            item.title = item.content_object
            item.titleAr = item.content_object.from_ageAr
            for i in cartItems:

                if i.content_object == item.content_object:
                    i.count += 1
                    i.save()
                    print(i.count)
                    return redirect("insurances")
            try:
                item.save()
                return redirect('insurances')
            except:
                return HttpResponse('opps!! item not added')




def insuranceDetails(request,insurance_id):
    insurance = get_object_or_404(Insurance,pk=insurance_id)
    return render(request,'insuranceDetails.html',{"insurance":insurance})

def insuranceDetailsAr(request,insurance_id):
    insurance = get_object_or_404(Insurance,pk=insurance_id)
    return render(request,'insuranceDetailAr.html',{"insurance":insurance})