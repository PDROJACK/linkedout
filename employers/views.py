from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def employers(request):
    return HttpResponse("List of all the employers")