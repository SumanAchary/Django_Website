from django import forms
from . forms import *
from . models import *
from cloudinary.forms import CloudinaryJsFileField, CloudinaryUnsignedJsFileField
from cloudinary.compat import to_bytes
import cloudinary, hashlib


class save_form_data(forms.ModelForm):
  class Meta:
  	model = users_details
  	fields = ('Name','Email','Phone','Password','avatar','Gender','country','otp','about')

class save_login_data(forms.ModelForm):
  class Meta:
  	model = login_details
  	fields = ('Email','Password')