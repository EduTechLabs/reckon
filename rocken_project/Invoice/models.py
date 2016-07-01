from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CompanyCreation(models.Model):
	companyName = models.CharField(max_length=100,null=False,blank =False)
	companyAddress = models.TextField(null=True,blank=True)
	city = models.CharField(max_length=100,null=True,blank =True)
	email = models.EmailField(null=True,blank = True)
	contactPersonName = models.CharField(max_length=100,null=True,blank =True)
	contactPersonNo = models.IntegerField(null=True,blank = True)
	def __unicode__(self):
		return self.companyName


class Client(models.Model):
	company = models.ForeignKey(CompanyCreation,null=True,blank=True)
	name = models.CharField(max_length=100,null=True,blank =True)
	invoiceName = models.CharField(max_length=100,null=True,blank =True)
	address = models.TextField(null=True,blank=True)
	clientContactPersonName =models.CharField(max_length=100,null=True,blank =True)
	clientContactPersonEmail =models.EmailField(null=True,blank = True)
	clientContactPersonNo = models.IntegerField(null=True,blank = True)
	termsAndConditions= models.TextField(null=True,blank=True)
	def __unicode__(self):
		return self.clientName



class Invoice(models.Model):
	client = models.ForeignKey(Client,null=True,blank=True)
	client_invoice_name_copy =  models.CharField(max_length=100,null=True,blank =True)
	clientAddresscopy = models.TextField(null=True,blank=True)
	contactPersonNamecopy = models.CharField(max_length=100,null=True,blank =True)
	contactPersonNocopy = models.IntegerField(null=True,blank = True)
	date = models.DateTimeField()
	serviceTaxRate = models.IntegerField(null=True,blank = True)
	termsAndConditionscopy= models.TextField(null=True,blank=True)

	def __unicode__(self):
		return self.client_invoice_name_copy

class InvoiceParticulars(models.Model):
	invoice =  models.ForeignKey(Invoice)
	particulars = models.TextField(null=True,blank=True)
	amount = models.IntegerField(null=True,blank =True)
	quantity = models.IntegerField(null=True,blank =True)
	periodInDays =models.IntegerField(null=True,blank =True)













