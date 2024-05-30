from .views  import RegistrationView, UsernameValidationView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt #se importa el decorador csrf_exempt que permite que la vista no requiera un token de seguridad

urlpatterns = [
  path('register', RegistrationView.as_view(), name="register"),
  path('validate-username', csrf_exempt(UsernameValidationView.as_view()), name="validate-username")
]
