from django.shortcuts import render,HttpResponse,render_to_response,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from models import CompanyCreation,Client,Invoice
from datetime import datetime

# Create your views here.

def login(request):
	return render_to_response("Template/Loginpage.html")

def invoice(request):
	return render_to_response("Invoice.html")


def homepage(request):
	company = CompanyCreation.objects.all()
	args = {}
	args['company'] = company
	return render_to_response('Homepage.html', args)

def auth(request):
	args={}
	if request.POST:
		print request.POST, "hello..."
		username = request.POST['username']
		password = request.POST['password']
		redirectUrl = '/Invoice/homepage/'
		args = {"username":username,"password":password}
		print args

		try:
			user = User.objects.get(username=username)
		except:
			print "username does not exist"
			args['validation'] = "username does not exist..!!"
			args['status'] = False
			return render_to_response('Template/Loginpage.html',args)
		if user.groups.filter(name='USER').exists():
			redirectUrl = '/Invoice/homepage/'

		print user

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				return HttpResponseRedirect(redirectUrl)
			else:
				validation = "Login invalid. Please try again."
				args = {}
				args['validation'] = validation
				args['status'] =False
				return HttpResponseRedirect('Loginpage.html', args)
		else:
			validation = "Login invalid. Please try again."
			args = {}
			args['validation'] = validation
			args['status'] =False
			return render_to_response('Template/Loginpage.html',args)
	else:
		return render_to_response('Template/Loginpage.html',args)


def clientlist(request,id):
	client = Client.objects.filter(company__id = id)
	args = {}
	args['client'] = client
	return render_to_response('clients.html',args)

def invoicePage(request):
	print request.POST
	if request.POST:
		print "hello"
		companyId = request.POST['companyId']
		client_invoice_name_copy = request.POST['client_invoice_name_copy']
		client_address_copy = request.POST['client_address_copy']
		contact_person_name_copy = request.POST['contact_person_name_copy']
		contact_person_no_copy  = request.POST['contact_person_no_copy ']
		date = request.POST['date']
		# status = request.POST['status']
		service_tax_rate = request.POST['service_tax_rate']
		terms_and_conditions_copy = request.POST['terms_and_conditions_copy']
		client = Client.objects.get(id=companyId)

		date = datetime.strptime(date,'%m/%d/%Y %H:%M:%S')

		c = Invoice(client = client,client_invoice_name_copy = client_invoice_name_copy,client_address_copy =client_address_copy,
			contact_person_name_copy = contact_person_name_copy,contact_person_no_copy =contact_person_no_copy,
			date  = date ,service_tax_rate = service_tax_rate,terms_and_conditions_copy = terms_and_conditions_copy
			)
		c.save()
		validation = "Registered successfully"
		args = {}
		args['validation'] = validation
		return render_to_response('Invoice.html',args)
	else:
		print "hi"
		clients = Client.objects.all()
		args = {}
		args['clients'] =clients
		return render_to_response('Invoice.html', args)







