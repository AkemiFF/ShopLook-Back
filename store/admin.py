from .models import *
from django.contrib import admin

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Invoice)
admin.site.register(InvoiceDetail)
