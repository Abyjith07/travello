from django.http import HttpResponse
from django.shortcuts import render

from .models import Place
from .models import Second

# Create your views here.
#def home(request):

 #   return render(request,"home.html")

#def about(request):
 #   return HttpResponse("About")
def home(request):
    obj=Place.objects.all()
    obj1=Second.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})

#def addition(request):
 #   x=int(request.GET['num1'])
  #  y=int(request.GET['num2'])
   # res1=x+y
    #res2=x-y
    #res3=x*y
    #res4=x/y
    #return render(request,"result.html",{'result1':res1,'result2':res2,'result3':res3,'result4':res4})

#def details(request):
 #    return HttpResponse("Details")

#def thanks(request):
 #   return HttpResponse("Thanks")