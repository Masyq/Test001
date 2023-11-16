
from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'index001.html')


def index1(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    responsestr = "username = {}, password = {}".format(username, password)
    temp = {"user":username, "pwd":password}
#    print(responsestr)
    return render(request, 'index002.html', {"data":temp})
