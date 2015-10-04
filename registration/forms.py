from django import forms

# Import the CaptchaField from 'django-simple-captcha'
from captcha.fields import CaptchaField

# Create form class for the Registration form
class RegistrationForm(forms.Form):
  name = forms.CharField()
  username = forms.CharField()
  email = forms.EmailField()
  password = forms.CharField(widget=forms.PasswordInput) # Set the widget to
                                                         # PasswordInput
  password2 = forms.CharField(widget=forms.PasswordInput,
                              label="Confirm password") # Set the widget to
                                                        # PasswordInput and
                                                        # set an appropriate
                                                        # label
  captcha = CaptchaField()
  
  # clean_<fieldname> method in a form class is used to do custom validation
  # for the field.
  # We are doing a custom validation for the 'password2' field and raising
  # a validation error if the password and its confirmation do not match
  def clean_password2(self):
    password = self.cleaned_data['password'] # cleaned_data dictionary has the
                                             # the valid fields
    password2 = self.cleaned_data['password2']
    if password != password2:
      raise forms.ValidationError("Passwords do not match.")
    return password2
