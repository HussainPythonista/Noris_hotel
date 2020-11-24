from django.shortcuts import render
from .models import AdminStuff

# Create your views here.
def home(request):
    rooms=AdminStuff.objects.all()
    context={'rooms':rooms}
    return render(request,'index.html',context)