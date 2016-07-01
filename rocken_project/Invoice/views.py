from django.shortcuts import render,HttpResponse,render_to_response,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.

def login(request):
	return render_to_response("Template/Loginpage.html")

def homepage(request):
	return render_to_response("Template/Homepage.html")

def auth(request):
	if request.POST:
		print request.POST, "hello..."
		username = request.POST['username']
		password = request.POST['password']

		redirectUrl = '/'
		args = {"username":username,"password":password}
		print args

		try:
			user = User.objects.get(username=username)
		except:
			print "username does not exist"
			args['validation'] = "Invalid login details..!!"
			args['status'] = False
			return render_to_response('Template/Loginpage.html',args)
		# if user.groups.filter(name='USER').exists():
		# 	redirectUrl = '/Registeruser/Reg/'
		if request.user.is_authenticated():
			redirectUrl = 'Invoice/homepage'


		else:
			print "user does not belong to the expected groups"
			args['validation'] = "Invalid login details..!!"
			args['status'] = False
			return render_to_response('Template/Loginpage.html',args)

		print user

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				# login(request, user)
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

