from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(clubname)
admin.site.register(category)
admin.site.register(product)
admin.site.register(blog)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Customer)