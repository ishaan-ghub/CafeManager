from django.contrib import admin
from .models import beverage, review, certificate, store

# Register your models here.

class reviewInline(admin.TabularInline):
    model= review
    extra= 2

class beverageAdmin(admin.ModelAdmin):
    list_display= ('name', 'type', 'date_added')
    inlines= [reviewInline]

class storeAdmin(admin.ModelAdmin):
    list_display= ('name', 'location')  
    filter_horizontal= ('drink_varieties',)

class certificateAdmin(admin.ModelAdmin):
    list_display= ('drink', 'certificate_no','issued_date','valid_untill')

admin.site.register(beverage,beverageAdmin)
admin.site.register(store, storeAdmin)
admin.site.register(certificate, certificateAdmin)

