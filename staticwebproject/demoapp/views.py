from django.shortcuts import render
from .models import place
from .models import kids
# Create your views here.

def demo(request):
    obj=place.objects.all()
    obj1=kids.objects.all()
    return render(request,"index.html",{'result':obj,'res':obj1})

