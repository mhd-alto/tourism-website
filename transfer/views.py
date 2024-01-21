from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import Car
from cart.models import Cart,CartItem
from django.contrib.auth.decorators import login_required


def Cars(request):
    cars = Car.objects.all()
    sCar = Car.objects.none
    drop = []
    ride = []
    pe = []
    ba = []
    for i in cars:
        r = i.ride_from
        ride.append(r)
        d = i.drop_off_to
        drop.append(d)
        p = i.Persons_number
        pe.append(p)
        b = i.bags_number
        ba.append(b)

    drop = [*set(drop)]
    ride = [*set(ride)]
    pe = [*set(pe)]
    ba = [*set(ba)]
    print(drop)
    print(ride)
    if request.method == "POST":
        rideFrom = request.POST.get('from')
        dropoff = request.POST.get('to')
        persons = request.POST.get('persons')
        bags = request.POST.get('bags')
        if (rideFrom and dropoff and persons and bags)!="-1":
            sCar = Car.objects.filter(ride_from=rideFrom,drop_off_to=dropoff)
            sCar = sCar.filter(Persons_number=persons)
            sCar = sCar.filter(bags_number=bags)
            print("1")
        if rideFrom !="-1" and dropoff !="-1" and persons !="-1" and bags == "-1":
            sCar = Car.objects.filter(ride_from=rideFrom,drop_off_to=dropoff)
            sCar = sCar.filter(Persons_number=persons)
            print("2")
        if rideFrom != "-1" and dropoff != "-1" and (persons and bags) =="-1" :
            sCar = Car.objects.filter(ride_from=rideFrom,drop_off_to=dropoff)
            print("3")
        if rideFrom != "-1" and persons !="-1":
            sCar = Car.objects.filter(ride_from=rideFrom)
            sCar = sCar.filter(Persons_number=persons)
            print('hi')
        if dropoff !="-1" and persons !="-1":
            sCar = Car.objects.filter(drop_off_to=dropoff)
            sCar = sCar.filter(Persons_number=persons)
            print('bay')
        if rideFrom != "-1" and dropoff =="-1" and persons == "-1" and bags == "-1":
            sCar = Car.objects.filter(ride_from=rideFrom)
            print("rideFrom")
        if dropoff != "-1" and rideFrom == "-1" and persons == "-1" and bags == "-1":
            sCar = Car.objects.filter(drop_off_to=dropoff)
            print("drop")

        print(f'R{rideFrom}___D{dropoff}____P{persons}___b{bags}')
        
    context = {"cars":cars,"sCar":sCar,"drop":drop,"ride":ride,"pe":pe,"ba":ba}
    return render(request,'Cars.html',context)


def CarsAr(request):
    cars = Car.objects.all()
    sCar = Car.objects.none
    drop = []
    ride = []
    pe = []
    ba = []
    for i in cars:
        r = i.ride_fromAr
        ride.append(r)
        d = i.drop_off_toAr
        drop.append(d)
        p = i.Persons_number
        pe.append(p)
        b = i.bags_number
        ba.append(b)

    drop = [*set(drop)]
    ride = [*set(ride)]
    pe = [*set(pe)]
    ba = [*set(ba)]
    if request.method == "POST":
        rideFrom = request.POST.get('from')
        dropoff = request.POST.get('to')
        persons = request.POST.get('persons')
        bags = request.POST.get('bags')
        if (rideFrom and dropoff and persons and bags)!="-1":
            sCar = Car.objects.filter(ride_fromAr=rideFrom,drop_off_toAr=dropoff)
            sCar = sCar.filter(Persons_number=persons)
            sCar = sCar.filter(bags_number=bags)
            print("1")
        if rideFrom !="-1" and dropoff !="-1" and persons !="-1" and bags == "-1":
            sCar = Car.objects.filter(ride_fromAr=rideFrom,drop_off_toAr=dropoff)
            sCar = sCar.filter(Persons_number=persons)
            print("2")
        if rideFrom != "-1" and dropoff != "-1" and (persons and bags) =="-1" :
            sCar = Car.objects.filter(ride_fromAr=rideFrom,drop_off_toAr=dropoff)
            print("3")
        if rideFrom != "-1" and persons !="-1":
            sCar = Car.objects.filter(ride_fromAr=rideFrom)
            sCar = sCar.filter(Persons_number=persons)
            print('hi')
        if dropoff !="-1" and persons !="-1":
            sCar = Car.objects.filter(drop_off_toAr=dropoff)
            sCar = sCar.filter(Persons_number=persons)
            print('bay')
        if rideFrom != "-1" and dropoff =="-1" and persons == "-1" and bags == "-1":
            sCar = Car.objects.filter(ride_fromAr=rideFrom)
            print("rideFrom")
        if dropoff != "-1" and rideFrom == "-1" and persons == "-1" and bags == "-1":
            sCar = Car.objects.filter(drop_off_toAr=dropoff)
            print("drop")

        print(f'R{rideFrom}___D{dropoff}____P{persons}___b{bags}')
        
    context = {"cars":cars,"sCar":sCar,"drop":drop,"ride":ride,"pe":pe,"ba":ba}
    return render(request,'CarsAr.html',context)


@login_required(login_url='login')
def addToCart(request,car_id):
    car = get_object_or_404(Car,pk=car_id)
    try:
        cart = Cart.objects.get(added_by=request.user,is_active=False)
        cartItems = CartItem.objects.filter(cart=cart)
        item = CartItem(content_object=car,object_id=car.id,cart=cart)
        item.titleAr = item.content_object.ride_fromAr
        item.title = item.content_object
        for i in cartItems:
            if i.content_object == item.content_object:
                i.count += 1
                i.save()
                print(i.count)
                return redirect("cars")
        try:
            item.save()
            return redirect('cars')
        except:
            return HttpResponse('opps!! item not added') 
    except:
        print('_________________________________________')
        cart = Cart(added_by=request.user,is_active=False)
        cart.save()
        cart = Cart.objects.get(added_by=request.user,is_active=False)
        cartItems = CartItem.objects.filter(cart=cart)
        if cart:
            item = CartItem(content_object=car,object_id=car.id,cart=cart)
            item.title = item.content_object
            for i in cartItems:
                if i.content_object.id == item.content_object.id:
                    i.count += 1
                    i.save()
                    print(i.count)
                    return redirect("cars")
            try:
                item.save()
                return redirect('cars')
            except:
                return HttpResponse('opps!! item not added')


def carsDetails(request,car_id):
    visa = get_object_or_404(Car,pk=car_id)
    return render(request,'transferDetails.html',{"car":visa})

def carsDetailsAr(request,car_id):
    visa = get_object_or_404(Car,pk=car_id)
    return render(request,'transferDetailsAr.html',{"car":visa})