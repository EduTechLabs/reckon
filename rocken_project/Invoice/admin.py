from django.contrib import admin
from models import CompanyCreation,Client,InvoiceParticulars,Invoice

# Register your models here.
admin.site.register(CompanyCreation)
admin.site.register(Client)
admin.site.register(InvoiceParticulars)
admin.site.register(Invoice)
