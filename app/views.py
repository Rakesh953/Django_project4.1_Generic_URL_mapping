from django.shortcuts import render

# Create your views here.
def temp(request):
    return render(request,'temp.html')

def temp1(request):
    return render(request,'temp1.html')