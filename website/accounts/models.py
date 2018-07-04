# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField



class users_details(models.Model):
 	Name = models.CharField(max_length = 25)
 	Email = models.CharField(max_length = 50)
 	Phone = models.CharField(max_length = 11)
 	Password = models.CharField(max_length =20)
 	Gender =  models.CharField(max_length =10,null = True, blank = True)
	avatar = CloudinaryField(null = True, blank = True)
	country = models.CharField(max_length =10,null = False, blank = True)
	otp =  models.CharField(max_length = 10,null = False, blank = True)
	about = models.CharField(max_length = 25,null = False, blank = True)


	

class login_details(models.Model):
 	Email = models.CharField(max_length = 50)
 	Password = models.CharField(max_length =20)
 	
