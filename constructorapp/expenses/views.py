from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'expenses/index.html') #renderizando el html index.html

def add_expense(request):
    return render(request, 'expenses/add_expense.html') #renderizando el html index.html