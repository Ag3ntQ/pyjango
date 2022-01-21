from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import member
from .forms import Myform


##########   "/"
def index(request):
	members=member.objects.all()
	return render(request,'index.html',{"members":members})
####	  /add
def add(request):
  if request.method == "POST":
    form = Myform(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = Myform()
  return render(request, 'form.html', {'form': form})
 ####  
def dlt(request,id):
   memdlt=member.objects.get(id=id)
   memdlt.delete()
   return redirect("/")
 ##### 
def bk(request):
	return redirect("/")