from __future__ import unicode_literals
from django.shortcuts import render , HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from . forms import *
from . models import *
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.views import View 
from django.core.mail import EmailMessage
import time
from django_otp.oath import totp
from django_otp.util import random_hex
import time
from twilio.rest import Client
from django.conf import settings



secret_key = b'1234567890123467890'
now = int(time.time())

# class logout(View):
# 	def get(request):
# 		logout(request)
# 		return render(request, 'home.html')

class home(View):
	def get(self,request):
		return render(request, 'home.html')

class reset_pass(View):
	def get(self,request):
		return render(request, 'otp_page.html')

class login(View):				
	def get(self,request):
		return render(request, 'login.html')

class signup(View):				
	def get(self,request):
		return render(request, 'signup.html')

class edit(View):
	def get(self,request,id):
		print('EDIT FUNCTION CALLED')
		p = users_details.objects.get(id = id)
		return render(request, 'edit.html',{'p':p})	

class send_otp(View):
	def post(self,request):
		print('send OTP  CALLED')
		user_email = request.POST['Email']
		data_user = users_details.objects.get(Email = user_email)
		phone = data_user.Phone
		print(phone)
		for delta in range(10,110,20):
			otp =(totp(key=secret_key, step=10, digits=6, t0=(now-delta)))		
		print('--IM SEND OTP--OTP IS =',otp,type(otp))
		client = Client(settings.TWILIO_ACCOUNT_STD, settings.TWILIO_AUTH_TOKEN)
		message = client.messages.create(to='+91'+str(phone), from_='+19143152078', body="your otp=" + str(otp))
		print(message.sid)
		email = EmailMessage('Suman Group of Hotels: Password Change',str(otp), to=[user_email])
		email.send()
		user = users_details.objects.get(Email = user_email)
		user.otp = otp
		user.save()
		return render(request, 'check_otp.html')

class check_OTP(View):
	def post(self,request):
		print('OTP CHECK CALLED')
		user_email = request.POST['CEmail']
		user_otp = request.POST['Cotp']
		p = users_details.objects.get(Email = user_email)
		otp_m = 'Done'
		print(user_email,'otp = ',user_otp)
		if users_details.objects.filter(Email = user_email).exists():
			if users_details.objects.filter(otp = user_otp).exists():
				print('Matching')
				return render(request, 'p_change.html',{'p':p})
					
			else:
				otp_m = 'OTP Didnt MATCH'
				return render(request, 'check_otp.html',{'otp_m':otp_m})
		else:
			e_m = 'Email Didnt Match'
			return render(request, 'check_otp.html',{'otp_m':otp_m})	
		return render(request, 'check_otp.html')

class login_data(View):
	def post(self,request):
		if request.method == 'POST':
			print("\n\n\ninside POST",request.POST)
			form = save_login_data(request.POST , request.FILES)
	  		if form.is_valid():
	  			print("\n\n\n inside login Database")
		  		login_cred = form.save()
		  		curent = form.save(commit=False)
	  			if users_details.objects.filter(Email = curent.Email).exists():
	  				if users_details.objects.filter(Password = curent.Password).exists():
	  					print('\n\n\n\n\n login Email  and Pass Found')
	  					index = users_details.objects.get(Email=curent.Email)
	  					D = login_details.objects.all()
	  					D.delete()
	  					print('login_cred Deleted Safely for security',index.Name)			
	  			else:
	  				print('Credentials Didnt Match')
	  				message= 'Opps! Email or Password was invalid'
	  				return render(request,'login.html',{'message':message})
		  		print("\n\nafter form")
		  		Data = users_details.objects.all()		  		 		
			else:
		 		print(form.errors) 		
			 	print("inside notValid\n\n\n") 		
		return render(request,'profile.html',{'index':index})

class update_pass(View):
	 def post(self,request,id):
		print('UPDATE_pass FUNCTION CALLED id =',id)
		if request.method == 'POST':
			print('inside POST')
			new_pass = request.POST['Password']
			print(new_pass)
			data_user = users_details.objects.get(id = id)
			# new_pass = data_user.Password
			# user = users_details.objects.get(Email = user_email)
			print('old password was = ',data_user.Password)
			data_user.Password = new_pass
			data_user.save()
			print('\n\n\n New password is = ',data_user.Password)
			Data = users_details.objects.all()
			return  render(request,'display_users.html', {'Data':Data})
		
class update(View):
	 def post(self,request,id):
		print('UPDATE_ FUNCTION CALLED id =',id)
		if request.method == 'POST':
			p = users_details.objects.get(id = id)
			form = save_form_data(request.POST or None,request.FILES or None,instance=p)
			if form.is_valid():
				form.save()
				Data = users_details.objects.all()
				return  render(request,'display_users.html', {'Data':Data})

class submitted(View):
	def post(self,request):
		CLOUDINARY_UPLOAD_PRESET ='dxgqmzu4'
		if request.method == 'POST':
			print("\n\n\ninside POST",request.POST)
			form = save_form_data(request.POST , request.FILES)
	  		if form.is_valid():
	  			print("\n\n\n inside IS_valid")
	  			instance = form.save(commit=False)
	  			if users_details.objects.filter(Email = instance.Email).exists():
	  				print('\n\n\n\n\n\nDuplicate Email Found')
	  				message = 'Email  already registered, please enter a new email'					
					return render(request,'signup.html',{'message':message})
	  			else:	  				
			  		form.save()
			  		print("\n\nafter form")
			  		Data = users_details.objects.all()
			  		print("\n\nDATA SUBMIT SUCCESFUL")  		
			else:
			 	print(form.errors) 		
			 	print("inside notValid\n\n\n") 		
		return render(request,'display_users.html', {'Data':Data})

class display_users(View):
	def get(self,request):
		Data = users_details.objects.all()
		return render(request, 'display_users.html',{'Data':Data})

class delete(View):
	def get(self,request,id):
			print("inside DELETE FUNCTIONS")
			s = users_details.objects.get(id=id)
			s.delete()
			Data = users_details.objects.all()
			return render(request,'display_users.html',{'Data':Data})