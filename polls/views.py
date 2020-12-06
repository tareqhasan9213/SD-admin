from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def card(request):
    return render(request,'card.html')

def chart(request):
    return render(request,'chart.html')

def table(request):
    return render(request,'table.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def password(request):
    return render(request,'password.html')