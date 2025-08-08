from django.contrib import admin
from .models import Flan

# Register your models here.

@admin.register(Flan)
class ProductoAdmin(admin.ModelAdmin):
    pass
