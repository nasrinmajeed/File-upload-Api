from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def main(request):

    if request.method == "POST":
        file= request.FILES['file']
        File.objects.create(file=file)

    return render(request, 'main.html')
