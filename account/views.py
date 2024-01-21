from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from account.models import Profile
from account.permissions import groups_only
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, UserRegistrationForm,ProfileEdit
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from mainpage.models import Message
from django.db.models import Q
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from cart.models import Cart
from mainpage.models import Message

#)___________________________reset password test____________________________________
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("account/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/password_reseted_form.html", context={"password_reset_form":password_reset_form})

#_______________________________________________________________________
def register(request):
    """Handles user registration to the website"""
    group = Group.objects.get(name='customer')
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            
            profile = Profile.objects.create(user=new_user,
                                             date_of_birth=profile_form.cleaned_data["date_of_birth"],
                                             gender=profile_form.cleaned_data["gender"],
                                             phone_number=profile_form.cleaned_data["phone_number"] 
                                             )
            if request.FILES:
                profile.picture = profile_form.files["picture"]
            profile.save()
            group.user_set.add(new_user)
            newUser = authenticate(username=user_form.cleaned_data['username'],
                                    password=user_form.cleaned_data['password'],
                                    )
            login(request, newUser)
            return redirect('index')

    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()
    context = {"user_form": user_form, "profile_form": profile_form}
    return render(request, "registration/register.html", context)


@login_required(login_url='login')
def profile(request):
    user = get_object_or_404(User,pk=request.user.id)
    try:
        profile = get_object_or_404(Profile,user=user)
        has_profil = True
    except:
        profile = Profile()
        has_profil = False
    if request.method == "POST":
        user_form = ProfileEdit(request.POST,instance=user)
        user_profile = ProfileForm(request.POST,request.FILES,instance=profile)
        if user_form.is_valid() and user_profile.is_valid():
            form = user_form.save(commit=False)
            form.save()
            if has_profil:
                if request.FILES:
                    user_profile.picture = request.FILES['picture']
                user_profile.save()
            else:
                profile = Profile(user=form,
                                                    date_of_birth=user_profile.cleaned_data["date_of_birth"],
                                                    gender=user_profile.cleaned_data["gender"],
                                                    phone_number=user_profile.cleaned_data["phone_number"]
                )
                if request.FILES:
                    profile.picture = request.FILES['picture']
                profile.save()
            return redirect('profile')
    carts = Cart.objects.filter(added_by=request.user).order_by('-created')
    user_form = ProfileEdit(instance=user)
    user_profile = ProfileForm(instance=profile)
    context = {"user_form":user_form,"user_profile":user_profile,"carts":carts,"profile":profile}

    return render(request,'profile.html',context)







@groups_only('Administrator','Manager')
def dashboard(request):
    packages_number = Package.objects.count
    visa_number = Visa.objects.count
    transfer_number = Car.objects.count
    insurance_number = Insurance.objects.count
    blog_number = Blog.objects.count
    message = Message.objects.all()[:5]
    context = {"packages_number":packages_number,"visa_number":visa_number,"transfer_number":transfer_number,
    "insurance_number":insurance_number,"blog_number":blog_number,"message":message
    } 
    return render(request,'dashboardIndex.html',context)

#_____________________________________mainpage________________________________________
from .models import Profile, Slider
from .forms import sliderForm


@groups_only('Administrator','Manager')
def slider(request):
    slides = Slider.objects.all().order_by("-id")
    return render(request,"mainPageManag\slider.html",{"slides":slides})


@groups_only('Administrator','Manager')
def messageDetails(request,message_id):
    mess = get_object_or_404(Message,pk=message_id)
    return render(request,"message.html",{"m":mess})



@groups_only('Administrator','Manager')
def addSlide(request):
    if request.method == "POST":
        form = sliderForm(request.POST,request.FILES)
        if form.is_valid():
            slide_form = form.save(commit=False)
            slide_form.author = request.user
            if request.FILES:
                slide_form.photo = request.FILES['sliderimg']
            slide_form.save()

            redirect('slideList')
    else:
        form = sliderForm()
    context = {"form":form}
    return render(request,"mainPageManag\\add.html",context)

@groups_only('Administrator','Manager')
def editSlide(request,slide_id,title):
    slide_to_edit = get_object_or_404(Slider,pk=slide_id)
    if request.method == "POST":
        form = sliderForm(request.POST,request.FILES,instance=slide_to_edit)
        if form.is_valid():
            slide_form = form.save(commit=False)
            slide_form.author = request.user
            if request.FILES:
                slide_form.photo = request.FILES['sliderimg']
            slide_form.save()
            return redirect('slideList')
    else:
        form = sliderForm(instance=slide_to_edit)
    context = {"form":form,"obj":slide_to_edit}
    return render(request,"mainPageManag\\edit.html",context)

@groups_only('Administrator','Manager')
def deleteSlide(request,slide_id):
    slide = get_object_or_404(Slider,pk=slide_id)
    slide.delete()
    return redirect('slideList')
#_______________________________WhyUs______________________________________________________
from .models import WhyUs
from .forms import WhyUsForm
@groups_only('Administrator','Manager')
def whyUs(request):
    whyUs_to_edit = WhyUs.objects.first()
    if request.method == "POST":
        if whyUs_to_edit:
            form = WhyUsForm(request.POST,request.FILES,instance=whyUs_to_edit)
            if form.is_valid():
                whyUs_form = form.save(commit=False)
                if request.FILES:
                    whyUs_form.photo = request.FILES['img']
                whyUs_form.save()
                return redirect('whyUs')    
        else:
            form = WhyUsForm(request.POST,request.FILES)
            if form.is_valid():
                whyUs_form = form.save(commit=False)
                if request.FILES:
                    whyUs_form.photo = request.FILES['img']
                whyUs_form.save()
                return redirect('whyUs')
    else:
        if whyUs_to_edit:
            form = WhyUsForm(instance=whyUs_to_edit)
        else:
            form = WhyUsForm()
    context = {"form":form}
    return render(request,"whyus\\whyUs.html",context)

#_________________________________FAQ______________________________________________
from .models import FAQ
from .forms import FAQForm


@groups_only('Administrator','Manager')
def faq(request):
    faq_to_edit = FAQ.objects.first()
    if request.method == "POST":
        if faq_to_edit:
            form = FAQForm(request.POST,instance=faq_to_edit)
            if form.is_valid():
                faq_form = form.save(commit=False)
                faq_form.save()
                return redirect('FAQ')    
        else:
            form = FAQForm(request.POST)
            if form.is_valid():
                faq_form = form.save(commit=False)
                faq_form.save()
                return redirect('FAQ')
    else:
        if faq_to_edit:
            form = FAQForm(instance=faq_to_edit)
        else:
            form = FAQForm()
    context = {"form":form}
    return render(request,"FAQ\\FAQ.html",context)
#_________________________________FAQ______________________________________________
from .models import FAQAR
from .forms import FAQARForm

@groups_only('Administrator','Manager')
def faqAR(request):
    faq_to_edit = FAQAR.objects.first()
    if request.method == "POST":
        if faq_to_edit:
            form = FAQARForm(request.POST,instance=faq_to_edit)
            if form.is_valid():
                faq_form = form.save(commit=False)
                faq_form.save()
                return redirect('FAQ')    
        else:
            form = FAQARForm(request.POST)
            if form.is_valid():
                faq_form = form.save(commit=False)
                faq_form.save()
                return redirect('FAQ')
    else:
        if faq_to_edit:
            form = FAQARForm(instance=faq_to_edit)
        else:
            form = FAQARForm()
    context = {"form":form}
    return render(request,"FAQ\\FAQ.html",context)




#____________________________Package_________________________________________________________
from packages.models import Package,PackageImg
from packages.forms import PackageForm,imgFormset,ImgForm

"""HANDLES PACKAGE CRUD"""


@groups_only('Administrator','Manager')
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


        
        a = Paginator(packages,10)
        page_number = request.GET.get('page')
        try:
            page_obj = a.get_page(page_number)
        except PageNotAnInteger:
            page_obj = a.page(1)
        except EmptyPage:
            page_obj = a.page(a.num_pages)
    context = {'packages':page_obj}
    return render(request,'packages\package_list.html',context)



@groups_only('Administrator','Manager')
def packageList(request):
    packages = Package.objects.all().order_by('-created')
    
    a = Paginator(packages,10)
    page_number = request.GET.get('page')
    try:
        page_obj = a.get_page(page_number)
    except PageNotAnInteger:
        page_obj = a.page(1)
    except EmptyPage:
        page_obj = a.page(a.num_pages)
    context = {'packages':page_obj}
    return render(request,'packages\package_list.html',context)


@groups_only('Administrator','Manager')
def addPackage(request):
    """Create A Package"""
    if request.method =='POST':
        form = PackageForm(request.POST,files=request.FILES)
        imgsformset = imgFormset(request.POST,files=request.FILES)
        imgsformset.prefix = "img"
        if form.is_valid() and imgsformset.is_valid():
            package_form = form.save(commit=False)
            package_form.author = request.user
            if request.FILES:
                package_form.photo = request.FILES["photo"]
            package_form.save()
            for imgform in imgsformset.cleaned_data:
                    if imgform:
                        pop = imgform['DELETE']
                        if pop:
                            continue    
                        image = imgform['img']
                        photo = PackageImg(Package=package_form,img=image)
                        photo.save()
            
            return redirect('packages')
        else:
            print(imgsformset.errors)
    else:
        form = PackageForm()
        imgsformset = imgFormset(queryset=PackageImg.objects.none())
        imgsformset.prefix = "img"
    context = {
        "form":form,"imgsformset":imgsformset      
    }
    return render(request,'packages\\add.html',context)

@groups_only('Administrator','Manager')
def editPackage(request,package_id,title):
    """Edit A Package"""
    Package_to_edit = get_object_or_404(Package,pk=package_id)
    if request.method == "POST":
        package_form = PackageForm(data=request.POST,files=request.FILES,instance=Package_to_edit)
        if package_form.is_valid():
            package_form.save(commit=False)
            package_form.author = request.user
            if request.FILES:
                try:            
                    package_form.photo = request.FILES["photo"]
                except:
                    package_form.photo = Package_to_edit.photo
            package_form.save()
            return redirect('packages')
    else:
        package_form = PackageForm(instance=Package_to_edit)
        package_imgs = PackageImg.objects.filter(Package=Package_to_edit)
        
    return render(request, "packages\edit.html", {"form": package_form,"package_imgs":package_imgs,"obj":Package_to_edit})

@groups_only('Administrator','Manager')
def deletePackage(request,package_id):
    package = get_object_or_404(Package,pk=package_id)
    package.delete()
    return redirect('packages')

#_______________________________________________________________________________
"""img package """

@groups_only('Administrator','Manager')
def deleteImgPackage(request,img_id,package_id,title):
    img = get_object_or_404(PackageImg,pk=img_id)
    text = "opps! not deleted"
    if(img.delete()):
        text = "Image Deleted!"
    return redirect('editPackage',package_id,title)

@groups_only('Administrator','Manager')
def addimg(request,package_id,title):
    package = Package.objects.get(id=package_id)
    if request.method == "POST":
        img_form = ImgForm(request.POST,files=request.FILES)
        if img_form.is_valid():
            if request.FILES:
                image = request.FILES['img']
            img_form = PackageImg(Package=package,img=image)
            img_form.save()
            return redirect('editPackage',package_id,title)
    else:
        img_form = ImgForm()
    return render(request,'packages\\addImg.html',context={"img_form":img_form,"title":title})


# def delete_duplicate(items):
#     for item in items:
#         for i in items:
#             if item.img == i.img \
#                     and i.id is not None and item.id is not None:
#                 if i.id != item.id:
#                     i.delete()
#______________________________________Tours_____________________________________________
from tours.models import Tour,TourImg
from tours.forms import TourForm,imgTourFormset,ImgTourForm



@groups_only('Administrator','Manager')
def searchTour(request):
    search_tour = request.POST.get('search')
    if request.method == "POST":
        # tours = Tour.objects.filter(Q(title__icontains = search_tour))
        # tours = tours.order_by("-updated")

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


        
        a = Paginator(tours,10)
        page_number = request.GET.get('page')
        try:
            page_obj = a.get_page(page_number)
        except PageNotAnInteger:
            page_obj = a.page(1)
        except EmptyPage:
            page_obj = a.page(a.num_pages)
    context = {'packages':page_obj}
    return render(request,'tours\\tour_list.html',context)


@groups_only('Administrator','Manager')
def tourList(request):
    tours = Tour.objects.all().order_by('-updated')
    
    a = Paginator(tours,10)
    page_number = request.GET.get('page')
    try:
        page_obj = a.get_page(page_number)
    except PageNotAnInteger:
        page_obj = a.page(1)
    except EmptyPage:
        page_obj = a.page(a.num_pages)
    context = {'packages':page_obj}
    return render(request,'tours\\tour_list.html',context)


@groups_only('Administrator','Manager')
def addTour(request):
    """Create A Package"""
    if request.method =='POST':
        form = TourForm(request.POST,files=request.FILES)
        imgsformset = imgTourFormset(request.POST,files=request.FILES)
        imgsformset.prefix = "img"
        if form.is_valid() and imgsformset.is_valid():
            tour_form = form.save(commit=False)
            tour_form.author = request.user
            if request.FILES:
                tour_form.photo = request.FILES["photo"]
            tour_form.save()
            for imgform in imgsformset.cleaned_data:
                    if imgform:
                        pop = imgform['DELETE']
                        if pop:
                            continue
                        image = imgform['img']
                        photo = TourImg(tour=tour_form,img=image)
                        photo.save()
            
            return redirect('tours')
        else:
            print(imgsformset.errors)
    else:
        form = TourForm()
        imgsformset = imgTourFormset(queryset=TourImg.objects.none())
        imgsformset.prefix = "img"
    context = {
        "form":form,"imgsformset":imgsformset      
    }
    return render(request,'tours\\add.html',context)


@groups_only('Administrator','Manager')
def editTour(request,tour_id,title):
    """Edit A tour"""
    tour_to_edit = get_object_or_404(Tour,pk=tour_id)
    if request.method == "POST":
        tour_form = TourForm(data=request.POST,files=request.FILES,instance=tour_to_edit)
        if tour_form.is_valid():
            tour_form.save(commit=False)
            tour_form.author = request.user
            if request.FILES:
                try:            
                    tour_form.photo = request.FILES["photo"]
                except:
                    tour_form.photo = tour_to_edit.photo
            tour_form.save()
            return redirect('tours')
    else:
        tour_form = TourForm(instance=tour_to_edit)
        tour_imgs = TourImg.objects.filter(tour=tour_to_edit)
        
    return render(request, "tours\edit.html", {"form":tour_form,"package_imgs":tour_imgs,"obj":tour_to_edit})


@groups_only('Administrator','Manager')
def deleteTour(request,tour_id):
    tour = get_object_or_404(Tour,pk=tour_id)
    tour.delete()
    return redirect('tours')

#_______________________________________________________________________________
"""img tour """
@groups_only('Administrator','Manager')
def deleteTourImg(request,img_id,tour_id,title):
    img = get_object_or_404(TourImg,pk=img_id)
    text = "opps! not deleted"
    if(img.delete()):
        text = "Image Deleted!"
    return redirect('editTour',tour_id,title)


@groups_only('Administrator','Manager')
def addTourimg(request,tour_id,title):
    tour = Tour.objects.get(id=tour_id)
    if request.method == "POST":
        img_form = ImgTourForm(request.POST,files=request.FILES)
        if img_form.is_valid():
            if request.FILES:
                image = request.FILES['img']
            img_form = TourImg(tour=tour,img=image)
            img_form.save()
            return redirect('editTour',tour_id,title)
    else:
        img_form = ImgTourForm()
    return render(request,'tours\\addImg.html',context={"img_form":img_form,"title":title})





#______________________________________visa______________________________________________
                
from visa.forms import VisaForm
from visa.models import Visa

@groups_only('Administrator','Manager')
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

        a = Paginator(visa,10)
        page_number = request.GET.get('page')
        try:
            page_obj = a.get_page(page_number)
        except PageNotAnInteger:
            page_obj = a.page(1)
        except EmptyPage:
            page_obj = a.page(a.num_pages)
    context = {'visas':page_obj}
    return render(request,'visa\\visa_list.html',context)


@groups_only('Administrator','Manager')
def visaList(request):
    visas = Visa.objects.all().order_by('-updated')
    a = Paginator(visas,10)
    page_number = request.GET.get('page')
    try:
        page_obj = a.get_page(page_number)
    except PageNotAnInteger:
        page_obj = a.page(1)
    except EmptyPage:
        page_obj = a.page(a.num_pages)
    context = {'visas':page_obj}
    return render(request,'visa\\visa_list.html',context)

@groups_only('Administrator','Manager')
def addVisa(request):
    if request.method == "POST":
        form = VisaForm(request.POST,request.FILES)
        if form.is_valid():
            visa_form = form.save(commit=False)
            visa_form.author = request.user
            if request.FILES:
                visa_form.photo = request.FILES["photo"]
            visa_form.save()

            return redirect('visaList')
    else:
        form = VisaForm()
    context = {"form":form}
    return render(request,"visa\\add.html",context)


@groups_only('Administrator','Manager')
def editVisa(request,visa_id,title):
    visa_to_edit = get_object_or_404(Visa,pk=visa_id) 
    if request.method == "POST":
        form = VisaForm(request.POST,request.FILES,instance=visa_to_edit)
        if form.is_valid():
            visa_form = form.save(commit=False)
            visa_form.author = request.user
            if request.FILES:
                visa_form.photo = request.FILES["photo"]
            visa_form.save()

            return redirect('visaList')
    else:
        form = VisaForm(instance=visa_to_edit)
    context = {"form":form,"obj":visa_to_edit}
    return render(request,"visa\\edit.html",context)

@groups_only('Administrator','Manager')
def deleteVisa(request,visa_id):
    visa = get_object_or_404(Visa,pk=visa_id)
    visa.delete()
    return redirect('visaList')


# _______________________________Transfer_____________________________________________________

from transfer.models import Car
from transfer.forms import TransferForm



@groups_only('Administrator','Manager')
def searchTransfer(request):
    search_car = request.POST.get('search')
    if request.method == "POST":
        if (Car.objects.filter(Q(ride_from__icontains = search_car) |
        Q(ride_fromAr__icontains = search_car))):
            print(1)
            car = Car.objects.filter(Q(ride_from__icontains = search_car) | 
            Q(ride_fromAr__icontains = search_car))
            car = car.order_by("-updated") 
            print(f'{car}___________________________-')

        elif(Car.objects.filter(Q(drop_off_to__icontains = search_car) | 
        Q(drop_off_toAr__icontains = search_car))):
            print(2)
            car = Car.objects.filter(Q(drop_off_to__icontains = search_car) | 
            Q(drop_off_toAr__icontains = search_car))
            car = car.order_by("-updated")
        else:
            car = Car.objects.none()
            print(3)
        print(f"{car}____________________________---")
        a = Paginator(car,10)
        page_number = request.GET.get('page')
        try:
            page_obj = a.get_page(page_number)
        except PageNotAnInteger:
            page_obj = a.page(1)
        except EmptyPage:
            page_obj = a.page(a.num_pages)
    context = {'Cars':page_obj}
    return render(request,'transfer\\car_list.html',context)

@groups_only('Administrator','Manager')
def carList(request):
    cars = Car.objects.all().order_by('-updated')
    a = Paginator(cars,10)
    page_number = request.GET.get('page')
    try:
        page_obj = a.get_page(page_number)
    except PageNotAnInteger:
        page_obj = a.page(1)
    except EmptyPage:
        page_obj = a.page(a.num_pages)
    context = {'Cars':page_obj}
    return render(request,'transfer\\car_list.html',context)

@groups_only('Administrator','Manager')
def addCar(request):
    if request.method == "POST":
        form = TransferForm(request.POST,request.FILES)
        if form.is_valid():
            car_form = form.save(commit=False)
            car_form.author = request.user
            if request.FILES:
                car_form.photo = request.FILES["photo"]
            car_form.save()

            return redirect('carList')
    else:
        form = TransferForm()
    context = {"form":form}
    return render(request,"transfer\\add.html",context)

def editCar(request,car_id,title):
    car_to_edit = get_object_or_404(Car,pk=car_id) 
    if request.method == "POST":
        form = TransferForm(request.POST,request.FILES,instance=car_to_edit)
        if form.is_valid():
            car_form = form.save(commit=False)
            car_form.author = request.user
            if request.FILES:
                car_form.photo = request.FILES["photo"]
            car_form.save()

            return redirect('carList')
    else:
        form = TransferForm(instance=car_to_edit)
    context = {"form":form,"obj":car_to_edit}
    return render(request,"transfer\\edit.html",context)

@groups_only('Administrator','Manager')
def deletecar(request,car_id):
    car = get_object_or_404(Car,pk=car_id)
    car.delete()
    return redirect('carList')

# ________________________________Insurance_________________________________________________

from insurance.models import Insurance
from insurance.forms import InsuranceForm

@groups_only('Administrator','Manager')
def searchInsurance(request):
    search_insurance = request.POST.get('search')
    if request.method == "POST":
        if (Insurance.objects.filter(Q(from_age__icontains = search_insurance) |
        Q(from_ageAr__icontains = search_insurance))):
            print(1)
            insurance = Insurance.objects.filter(Q(from_age__icontains = search_insurance) | 
            Q(from_ageAr__icontains = search_insurance))
            insurance = insurance.order_by("-updated") 
            print(f'{insurance}___________________________-')

        elif(Insurance.objects.filter(Q(to_age__icontains = search_insurance) | 
        Q(to_ageAr__icontains = search_insurance))):
            print(2)
            insurance = Insurance.objects.filter(Q(to_age__icontains = search_insurance) | 
            Q(to_ageAr__icontains = search_insurance))
            insurance = insurance.order_by("-updated")
        else:
            insurance = Insurance.objects.none()
            print(3)
        print(f"{insurance}____________________________---")
        a = Paginator(insurance,10)
        page_number = request.GET.get('page')
        try:
            page_obj = a.get_page(page_number)
        except PageNotAnInteger:
            page_obj = a.page(1)
        except EmptyPage:
            page_obj = a.page(a.num_pages)
    context = {'insurances':page_obj}
    return render(request,'insurance\\Insurance_list.html',context)


@groups_only('Administrator','Manager')
def insuranceList(request):
    insurance = Insurance.objects.all().order_by('-updated')
    a = Paginator(insurance,10)
    page_number = request.GET.get('page')
    try:
        page_obj = a.get_page(page_number)
    except PageNotAnInteger:
        page_obj = a.page(1)
    except EmptyPage:
        page_obj = a.page(a.num_pages)
    context = {'insurances':page_obj}
    return render(request,'insurance\\Insurance_list.html',context)

@groups_only('Administrator','Manager')
def addInsurance(request):
    if request.method == "POST":
        form = InsuranceForm(request.POST)
        if form.is_valid():
            insurance_form = form.save(commit=False)
            insurance_form.author = request.user
            insurance_form.save()
            return redirect('insuranceList')
    else:
        form = InsuranceForm()
    context = {"form":form}
    return render(request,"insurance\\add.html",context)

@groups_only('Administrator','Manager')
def editInsurance(request,insurance_id,title):
    insurance_to_edit = get_object_or_404(Insurance,pk=insurance_id) 
    if request.method == "POST":
        form = InsuranceForm(request.POST,instance=insurance_to_edit)
        if form.is_valid():
            insurance_form = form.save(commit=False)
            insurance_form.author = request.user
            insurance_form.save()
            return redirect('insuranceList')
    else:
        form = InsuranceForm(instance=insurance_to_edit)
    context = {"form":form,"obj":insurance_to_edit}
    return render(request,"insurance\\edit.html",context)


@groups_only('Administrator','Manager')
def deleteInsurance(request,insurance_id):
    insurance = get_object_or_404(Insurance,pk=insurance_id)
    insurance.delete()
    return redirect('insuranceList')

#-------------------BLOG-----------------------
from .models import Blog
from .forms import BlogForm
from django.utils.text import slugify

@groups_only('Administrator','Manager')
def searchBlog(request):
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
    context = {'blog':page_obj}
    return render(request,'blog\\blog_list.html',context)


@groups_only('Administrator','Manager')
def BlogList(request):
    blog = Blog.objects.all().order_by('-id')
    a = Paginator(blog,10)
    page_number = request.GET.get('page')
    try:
        page_obj = a.get_page(page_number)
    except PageNotAnInteger:
        page_obj = a.page(1)
    except EmptyPage:
        page_obj = a.page(a.num_pages)
    context = {'blog':page_obj}
    return render(request,'blog\\blog_list.html',context)

@groups_only('Administrator','Manager')
def addBlog(request):
    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog_form = form.save(commit=False)
            blog_form.author = request.user
            blog_form.slug = slugify(blog_form.title)
            if request.FILES:
                blog_form.photo = request.FILES['photo']
            blog_form.save()

            form.save_m2m()
            return redirect('blogList')
    else:
        form = BlogForm()
    context = {"form":form}
    return render(request,"blog\\add.html",context)

@groups_only('Administrator','Manager')
def editBlog(request,blog_id,slug):
    blog_to_edit = get_object_or_404(Blog,pk=blog_id)
    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES,instance=blog_to_edit)
        if form.is_valid():
            blog_form = form.save(commit=False)
            blog_form.author = request.user
            blog_form.slug = slugify(blog_form.title)
            blog_form.slugAr = slugify(blog_form.titleAr)
            if request.FILES:
                blog_form.photo = request.FILES['photo']
            blog_form.save()

            form.save_m2m()
            return redirect('blogList')
    else:
        form = BlogForm(instance=blog_to_edit)
    context = {"form":form,"obj":blog_to_edit}
    return render(request,"blog\\edit.html",context)


@groups_only('Administrator','Manager')    
def deleteBlog(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    blog.delete()
    return redirect('blogList')

# #___________________________________________________________
# from cart.models import CartItem

# def test(request):
#     testa = []
#     c =  CartItem.objects.all()
#     for i in c:
#         if request.user == i.content_object.author:
#             print(i.content_object)
#             return HttpResponse(i.content_object.photo.url)
#         return HttpResponse()

    







