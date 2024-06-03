from django.shortcuts import render #se importa la funcion render que permite renderizar un template
from django.views import View #se importa la clase View de django que permite crear vistas basadas en clases
import json #se importa la libreria json que permite trabajar con archivos json
from django.http import JsonResponse #se importa la clase JsonResponse que permite retornar una respuesta en formato json
from django.contrib.auth.models import User #se importa el modelo User de la aplicacion auth de django. Permite interactuar con la tabla de usuarios de la base de datos
# Create your views here.

#la siguiente clase se encarga de validar el username, en caso de que no sea alfanumerico se retorna un mensaje de error.
class UsernameValidationView(View):
  def post(self, request):#se recibe la peticion
    data=json.loads(request.body) #se convierte el json a un diccionario
    username=data['username']#se obtiene el username

    if not str(username).isalnum():#se verifica si el username es alfanumerico
      return JsonResponse({'username_error': 'El nombre de usuario solo debe tener caracteres alfanuemericos'}, status=400)
    
    if User.objects.filter(username=username).exists(): #se verifica si el username ya existe en la base de datos
      return JsonResponse({'username_error': 'El nombre de usuario ya existe, escoja otro'}, status=409)
    
    return JsonResponse({'username_valid': True})
  
  #objetivo es comunicar el front y el back por medio de ajax para saber si se puede o no crear un usuario
  
class RegistrationView(View):
  """
  A view for handling user registration.

  This view renders the registration form template when accessed via GET request.
  """
  def get(self, request):
    return render(request, 'authentication/register.html')
