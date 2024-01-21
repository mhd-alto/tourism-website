from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/',views.profile,name='profile'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_changed_done.html'),
         name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),

    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password/password_reset_confirm.html'), name='password_reset_confirm'),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'),
         name='password_reset_complete'),
    path('reset/', auth_views.PasswordResetView.as_view(template_name='password/password_reseted_form.html')
         , name='password_reset'),
        
        
        
#   --------------------------DASHBOARD-------------------------


    path('d/',views.dashboard,name='d'),
#   --------------------------MainPage---------------------
#   ---
#   --
#   -
    path('sliderManagement/',views.slider,name="slideList"),
    path('addSlide/',views.addSlide,name="addSlide"),
    path('editSlide/<int:slide_id>/<str:title>',views.editSlide,name="editSlide"),
    path('deleteSlide/<int:slide_id>',views.deleteSlide,name="deleteSlider"),

    path('whyUs/',views.whyUs,name="whyUs"),

    path('FAQ/',views.faq,name="FAQ"),
    path('FAQAr/',views.faqAR,name="FAQAr"),
#   -   
#   --
#   --- 
#   --------------------------------------------------------
#   -------------------------Package------------------------
#   ---
#   --
#   -
    path('packageListSearch/',views.searchPackage,name='searchPackage'),
    path('packageList/',views.packageList,name='packages'),
    path('addPackage/',views.addPackage,name='addPackage'),
    path('editPackage/<int:package_id>/<str:title>',views.editPackage,name='editPackage'),
    path('deletePackage/<int:package_id>/',views.deletePackage,name='deletePackage'),
    path('deletePackageImg/<int:img_id>/<int:package_id>/<str:title>',views.deleteImgPackage,name="deletePackageImg"),
    path('addPackageImg/<int:package_id>/<str:title>',views.addimg,name="addImg"),
#   -   Tours
    path('tourListSearch/',views.searchTour,name='searchTour'),
    path('tourList/',views.tourList,name='tours'),
    path('addtour/',views.addTour,name='addTour'),
    path('editTour/<int:tour_id>/<str:title>',views.editTour,name='editTour'),
    path('deleteTour/<int:tour_id>/',views.deleteTour,name='deleteTour'),
    path('deleteTourImg/<int:img_id>/<int:tour_id>/<str:title>',views.deleteTourImg,name="deleteTourImg"),
    path('addToureImg/<int:tour_id>/<str:title>',views.addTourimg,name="addTourImg"),
#   -   
#   --
#   --- 
#   --------------------------------------------------------
# _______________________________VISA____________________________________________
    path('searchVisa/',views.searchVisa,name='searchVisa'),
    path('visaList/',views.visaList,name='visaList'),
    path('addVisa/',views.addVisa,name='addVisa'),
    path('editVisa/<int:visa_id>/<str:title>/',views.editVisa,name='editVisa'),
    path('deleteVisa/<int:visa_id>/',views.deleteVisa,name="deleteVisa"),
#     ________________________________transfer_______________________________________________
    path('searchCars/',views.searchTransfer,name='searchCars'),
    path('carList/',views.carList,name='carList'),
    path('addCar/',views.addCar,name='addCar'),
    path('editCar/<int:car_id>/<str:title>',views.editCar,name='editCar'),
    path('deleteCar/<int:car_id>/',views.deletecar,name='deleteCar'),
#    __________________________________Insurance________________________
#    _____
#    __
#    _
    path('searchInsurance/',views.searchInsurance,name='searchInsurance'),
    path('insuranceList/',views.insuranceList,name='insuranceList'),
    path('addInsurance/',views.addInsurance,name='addInsurance'),
    path('editInsurance/<int:insurance_id>/<str:title>',views.editInsurance,name='editInsurance'),
    path('deleteInsurance/<int:insurance_id>/',views.deleteInsurance,name='deleteInsurance'),
#                                                                       __
#                                                                    _____
#                                                                  _______
#   __________________________________blog____________________________________
    path('blogList/',views.BlogList,name='blogList'),
    path('searchBlog/',views.searchBlog,name='searchBlog'),
    path('addBlog/',views.addBlog,name='addblog'),
    path('editBlog/<int:blog_id>/<str:slug>',views.editBlog,name='editBlog'),
    path('deleteBlog/<int:blog_id>/',views.deleteBlog,name='deleteBlog'),
    path('message/<int:message_id>/',views.messageDetails,name='messageDetails'),


    ]