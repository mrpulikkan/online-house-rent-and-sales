from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(product)
admin.site.register(tag)
admin.site.register(orders)


