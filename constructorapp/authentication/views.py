from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
# Create your views here.

#la siguiente clase se encarga de validar el username, en caso de que no sea alfanumerico se retorna un mensaje de error.
class UsernameValidationView(View):
  def post(self, request):#se recibe la peticion
    data=json.loads(request.body) #se convierte el json a un diccionario
    username=data['username']#se obtiene el username

    if not str(username).isalnum():#se verifica si el username es alfanumerico
      return JsonResponse({'username_error': 'El nombre de usuario solo debe tener caracteres alfanuemericos'}, status=400)
    
    if not str(username).isalnum():#se verifica si el username es alfanumerico
      return JsonResponse({'username_error': 'El nombre de usuario solo debe tener caracteres alfanuemericos'}, status=400)
    
    
    
    
    
    
    return JsonResponse({'username_valid': True})
  
  #objetivo es la comuncacuoin entre el front y el back por medio de ajax para saber si se puede o no crear un usuario
  
class RegistrationView(View):
  """
  A view for handling user registration.

  This view renders the registration form template when accessed via GET request.
  """
  def get(self, request):
    return render(request, 'authentication/register.html')
