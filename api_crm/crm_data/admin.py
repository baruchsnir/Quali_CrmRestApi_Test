from django.contrib import admin
from .models import Accounts,Department,Product,Opportunities,Contacts,Service
# Register your models here.

admin.site.register(Accounts)
admin.site.register(Department)
admin.site.register(Product)
admin.site.register(Opportunities)
admin.site.register(Contacts)
admin.site.register(Service)
