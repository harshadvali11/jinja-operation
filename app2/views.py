from django.shortcuts import render

# Create your views here.


def specific_temp(request):
    return render(request,'specific_temp.html')