from django.shortcuts import render

# Create your views here.

def temp1(request):
    return render(request,'temp1.html',context={'a':111,'b':1111})

def temp2(request):
    return render(request,'temp2.html')