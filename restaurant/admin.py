from django.contrib import admin
from .models import BookingModel,MenuModel

# Register your models here.
admin.site.register(BookingModel)
admin.site.register(MenuModel)