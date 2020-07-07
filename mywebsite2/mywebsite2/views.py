from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'name': 'Alex', 'college': 'MMMUT'})


def details(request):
    return render(request, 'details.html')


def about(request):
    login = request.GET['username']
    pwd = request.GET['pass']

    if login == 'Akshay' and pwd == 'pass':
        return render(request, 'about.html', {'user': login})
    elif pwd == 'pass':
        return render(request, 'home.html', {'errormsg': 'Your username is wrong'})
    else:
        return render(request, 'home.html', {'errormsg': 'Please enter valid password'})


