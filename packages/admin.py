from django.contrib import admin
from .models import Package,PackageImg

class PackageImgAdmin(admin.StackedInline):
    model = PackageImg


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    inlines = [PackageImgAdmin] 