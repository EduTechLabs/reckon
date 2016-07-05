from django.shortcuts import render,render_to_response, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import  HttpResponseRedirect
from Invoice.models import CompanyCreation

# Create your views here.
def login(request):
	return render_to_response("Login.html")

def homepage(request):
	company = CompanyCreation.objects.all()
	args = {}
	args['company'] = company
	return render_to_response("Homepage.html",args)


def auth(request):
	if request.POST:
		print request.POST, "hello..."
		username = request.POST['username']
		password = request.POST['password']

		redirectUrl = ''
		args = {"username":username,"password":password}
		print args

		try:
			user = User.objects.get(username=username)
		except:
			print "username does not exist"
			args['validation'] = "Invalid login details..!!"
			args['status'] = False
			return render_to_response('Login.html',args)
		if user.groups.filter(name='USER').exists():
			redirectUrl = '/Invoice/homepage/'

		else:
			print "user does not belong to the expected groups"
			args['validation'] = "Invalid login details..!!"
			args['status'] = False
			return render_to_response('Login.html',args)

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
				return HttpResponseRedirect('Login.html', args)
		else:
			validation = "Login invalid. Please try again."
			args = {}
			args['validation'] = validation
			args['status'] =False
			return render_to_response('Login.html',args)
	else:
		return render_to_response('Login.html')

# # def client(request,pk=id)
# def clients(request, companyId=None):
# 	print companyId
# 	clientqry = CompanyCreation.objects.get(id=companyId)

# 	args = {"clientqry":clientqry}

# 	return render_to_response('client.html',args)

def client(request, id): 
	l =  CompanyCreation.objects.get(pk=id) 
	return render_to_response('client.html', {'CompanyCreation':l})
