from .views  import RegistrationView, UsernameValidationView, EmailValidationView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt#se importa el decorador csrf_exempt que permite que la vista no requiera un token de seguridad

urlpatterns = [
  path('register', RegistrationView.as_view(), name="register"),
  path('validate-username', csrf_exempt(UsernameValidationView.as_view()), #csrf_exempt se encarga de deshabilitar la proteccion csrf, lo cual permite que la vista pueda ser accedida sin un token de seguridad
      name="validate-username"),
  path('validate-email', csrf_exempt(EmailValidationView.as_view()), 
      name="validate-email")
]
