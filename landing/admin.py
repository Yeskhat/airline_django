from django.contrib import admin
from .models import *
# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
    list_filter= ["name", ]
    search_fields = ["name", "email"]

    class Meta:
        model = Client

admin.site.register(Client, ClientAdmin)