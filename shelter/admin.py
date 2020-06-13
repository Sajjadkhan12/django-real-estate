from django.contrib import admin
from .models import Listening,Quickcontact

# Register your models here.
class ListeningAdmin(admin.ModelAdmin):
    list_display = ('title','agent','location','price','area','bedrooms','bathrooms','available','status')
    search_fields = ['title','location','price']
    list_filter = ('agent',)
admin.site.register(Listening,ListeningAdmin)
admin.site.register(Quickcontact)

