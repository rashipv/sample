from django.http import HttpResponse
from django.shortcuts import render
from . models import place,table
# Create your views here.



def demo(request):
   obj=place.objects.all()
   cok=table.objects.all()
   return  render(request,"index.html",{'result':obj,'fine':cok})


