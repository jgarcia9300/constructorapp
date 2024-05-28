from django.shortcuts import render
from django.views import View

# Create your views here.

class RegistrationView(View):
  """
  A view for handling user registration.

  This view renders the registration form template when accessed via GET request.
  """
  def get(self, request):
    return render(request, 'authentication/register.html')
