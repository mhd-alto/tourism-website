from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Blog,WhyUs,FAQ,Profile

# Register your models here.
admin.site.register(Blog)
admin.site.register(WhyUs)
admin.site.register(FAQ)
admin.site.register(Profile)

