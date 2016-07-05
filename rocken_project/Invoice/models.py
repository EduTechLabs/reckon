from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CompanyCreation(models.Model):
	companyName = models.CharField(max_length=100, null = False,blank=False)
	contactPerson = models.CharField(max_length=100,null = True,blank=True)
	address = models.TextField(max_length=100,null = True,blank=True)
	city = models.CharField(max_length=100,null = True,blank=True)
	email = models.CharField(max_length=100,null = True,blank=True)
	contactNo = models.IntegerField(null = True,blank=True)

	def __unicode__(self):
		return self.companyName



class Client(models.Model):
	company =  models.ForeignKey(CompanyCreation)
	name = models.CharField(max_length=100,null = True,blank=True)
	address = models.TextField(null = True,blank = True)
	contact_person_name = models.CharField(max_length=100,null = True,blank=True)
	contact_person_email = models.EmailField()
	contact_person_no = models.IntegerField(null = True,blank=True)

	def __unicode__(self):
		return self.name


class InvoiceParticulars(models.Model):
	particular = models.CharField(max_length=100,null = True,blank=True)
	amount = models.IntegerField()
	quantity = models.IntegerField()
	period = models.CharField(max_length=100,null = True,blank=True)

	def __unicode__(self):
		return self.particular

class Invoice(models.Model):
	company_name_copy = models.CharField(max_length=100,null = True,blank=True)
	company_name_address_copy = models.CharField(max_length=100,null = True,blank=True)
	client_name = models.CharField(max_length=100,null = True,blank=True)
	client_Address = models.TextField(null = True,blank = True)
	contact_person_name_copy = models.CharField(max_length=100,null = True,blank=True)
	contact_person_email_copy = models.EmailField()
	contact_person_no_copy = models.IntegerField(null = True,blank=True)
	particulars = models.ForeignKey(InvoiceParticulars)
	service_tax_rate = models.IntegerField()
	Service_tax_amount = models.IntegerField()

	def __unicode__(self):
		return self.company_name_copy
	



	
		