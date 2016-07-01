from django.contrib import admin
from models import CompanyCreation,Client,Invoice,InvoiceParticulars
# Register your models here.
admin.site.register(CompanyCreation)
admin.site.register(Client)
admin.site.register(Invoice)
admin.site.register(InvoiceParticulars)

