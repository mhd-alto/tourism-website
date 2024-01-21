from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('AR/',views.indexAr,name='indexAr'),
    path('blogs/',views.blogs,name='blogs'),
    path('searchBlogs/',views.searchBlog,name='searchBlogu'),
    path('searchBlogsAr/',views.searchBlogAr,name='searchBlogAr'),
    path('مقالات/',views.blogsAr,name='blogsAr'),
    path('مقالات/<int:blog_id>/<str:slug>',views.blogDetailsAr,name='blogsDetailsAr'),
    path('blogs/<int:blog_id>/<str:slug>',views.blogDetails,name='blogsDetails'),
 
]