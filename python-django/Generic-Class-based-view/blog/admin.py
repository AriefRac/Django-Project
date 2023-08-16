from django.contrib import admin
from .models import Artikel
# Register your models here.

class ArtikelView(admin.ModelAdmin):
    readonly_fields = [
        'publish',
        'update',
        'slug',
    ]
    
admin.site.register(Artikel, ArtikelView)