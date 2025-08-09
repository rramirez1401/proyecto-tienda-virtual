from django.contrib import admin
from .models import Flan, ContactForm

# Register your models here.

@admin.register(Flan)
class ProductoAdmin(admin.ModelAdmin):
    pass

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    pass
