from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt 
def users(request):

    if(request.method == 'GET'):
        users = User.objects.all()
        print(users)
        return HttpResponse(users)

    elif(request.method == 'POST'):
        # print(request.POST["name"])
        User.post(request=request)
        return HttpResponse("success")


