from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
   # return HttpResponse("this is a homepage")
   context={
       'variable':"this is sent"
   }
   return render(request, 'index.html', context)
def about(request):
   # return HttpResponse("this is About")
   return render(request, 'about.html')
def services(request):
   # return HttpResponse("this is services")
   return render(request, 'services.html')
def contact(request):
    if request.method== "POST":
       email=request.POST.get('email')
       password=request.POST.get('password')
       address=request.POST.get('address')
       city=request.POST.get('city')

       contact=Contact(email=email, password=password, address=address, city=city)
       contact.save()
       messages.success(request, "Profile details updated.")


    


    return render(request, 'contact.html')
  #  return HttpResponse("this is contact")
