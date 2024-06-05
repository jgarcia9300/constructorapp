from django.shortcuts import render #se importa la funcion render que permite renderizar un template
from django.views import View #se importa la clase View de django que permite crear vistas basadas en clases
import json #se importa la libreria json que permite trabajar con archivos json
from django.http import JsonResponse #se importa la clase JsonResponse que permite retornar una respuesta en formato json
from django.contrib.auth.models import User #se importa el modelo User de la aplicacion auth de django. Permite interactuar con la tabla de usuarios de la base de datos
# Create your views here.
from validate_email import validate_email #se importa la funcion validate_email que permite validar si un email es valido
from django.contrib import messages #se importa la libreria messages que permite enviar mensajes de exito o error

#la siguiente clase se encarga de validar el email. Si el email no es valido, se retorna un mensaje de error. Si el email ya esta en uso, se retorna un mensaje de error
class EmailValidationView(View):
  #objetivo es comunicar el front y el back por medio de ajax para saber si se puede o no registrar un email
  def post(self, request):#se recibe la peticion
    data=json.loads(request.body) #se convierte el json a un diccionario
    email=data['email']#se obtiene el email

    if not validate_email(email):#se verifica si el email es valido
      return JsonResponse({'email_error': 'Email invalido'}, status=400)
    
    if User.objects.filter(email=email).exists(): #se verifica si el email ya existe en la base de datos
      return JsonResponse({'email_error': 'El email ya esta en uso, escoja otro'}, status=409)
    
    return JsonResponse({'username_valid': True})
  
class UsernameValidationView(View):
  #objetivo es comunicar el front y el back por medio de ajax para saber si se puede o no crear un usuario
  def post(self, request):#se recibe la peticion
    data=json.loads(request.body) #se convierte el json a un diccionario
    username=data['username']#se obtiene el email

    if not str(username).isalnum():#se verifica si el username es alfanumerico
      return JsonResponse({'username_error': 'El nombre de usuario solo debe tener caracteres alfanumericos'}, status=400)
    
    if User.objects.filter(username=username).exists(): #se verifica si el username ya existe en la base de datos
      return JsonResponse({'username_error': 'El nombre de usuario ya existe, escoja otro'}, status=409)
    
    return JsonResponse({'username_valid': True})
  
  
class RegistrationView(View):
  """
  A view for handling user registration.

  This view renders the registration form template when accessed via GET request.
  """
  def get(self, request):
    return render(request, 'authentication/register.html')
  
  def post(self, request):
    # obtener datos del usuario
    # Validar
    # Crear cuenta de usuario

    username = request.POST ['username'] 
    email = request.POST ['email']
    password = request.POST ['password']
