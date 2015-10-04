from django.shortcuts import render
from django.contrib.auth.models import User

from .forms import RegistrationForm

def registration_form(request):
  # If the request method is POST, it means that the form has been submitted
  # and we need to validate it.
  if request.method == 'POST':
    # Create a RegistrationForm instance with the submitted data
    form = RegistrationForm(request.POST)
    
    # is_valid validates a form and returns True if it is valid and
    # False if it is invalid.
    if form.is_valid():
      user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            email=form.cleaned_data['email']
            )
      return render(request, "registration/success.html")
 
 # This means that the request is a GET request. So we need to
 # create an instance of the RegistrationForm class and render it in
 # the template
  else:
   form = RegistrationForm()
 
 # Render the registration form template with a RegistrationForm instance. If the
 # form was submitted and the data found to be invalid, the template will
 # be rendered with the entered data and error messages. Otherwise an empty
 # form will be rendered. Check the comments in the registration_form.html template
 # to understand how this is done.
  return render(request, "registration/registration_form.html",
                { "form" : form })
