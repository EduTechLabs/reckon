from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CompanyCreation(models.Model):
	company_name = models.CharField(max_length=100,null=False,blank =False)
	company_address = models.TextField(null=True,blank=True)
	city = models.CharField(max_length=100,null=True,blank =True)
	email = models.EmailField(null=True,blank = True)
	contact_person_name = models.CharField(max_length=100,null=True,blank =True)
	contact_person_no = models.IntegerField(null=True,blank = True)
	def __unicode__(self):
		return self.company_name


class Client(models.Model):
	company = models.ForeignKey(CompanyCreation,null=True,blank=True)
	name = models.CharField(max_length=100,null=True,blank =True)
	invoice_name = models.CharField(max_length=100,null=True,blank =True)
	address = models.TextField(null=True,blank=True)
	client_contact_person_name = models.CharField(max_length=100,null=True,blank =True)
	client_contact_person_email =models.EmailField(null=True,blank = True)
	client_contact_person_no = models.IntegerField(null=True,blank = True)
	terms_and_conditions= models.TextField(null=True,blank=True)
	def __unicode__(self):
		return self.name


# choice = (
#       ('statuspending', 'Status Pending'),
#       ('sendtoclient', 'sendToclient'),
#       ('cancelled', 'Cancelled'),
#       ('amountreceived', 'Amount Received'),
#       ('partialamountreceived', 'PartialAmountReceived'),)

class Invoice(models.Model):
	client = models.ForeignKey(Client,null=True,blank=True)
	client_invoice_name_copy =  models.CharField(max_length=100,null=True,blank =True)
	client_address_copy = models.TextField(null=True,blank=True)
	contact_person_name_copy = models.CharField(max_length=100,null=True,blank =True)
	contact_person_no_copy = models.IntegerField(null=True,blank = True)
	date = models. DateField()
	# status = models.CharField(max_length=25,choices=choice,default='statuspending')
	service_tax_rate = models.IntegerField(null=True,blank = True)
	terms_and_conditions_copy= models.TextField(null=True,blank=True)

	def __unicode__(self):
		return self.client_invoice_name_copy

class InvoiceParticulars(models.Model):
	invoice =  models.ForeignKey(Invoice)
	particulars = models.TextField(null=True,blank=True)
	amount = models.IntegerField(null=True,blank =True)
	quantity = models.IntegerField(null=True,blank =True)
	period_in_days =models.IntegerField(null=True,blank =True)
	def __unicode__(self):
		return self.particulars













