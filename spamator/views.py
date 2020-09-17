from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def checksms(request):
    sms=request.POST.get('smstext','Guest')
    result=sms
    if result == '1':  #Ham
        return HttpResponse('ham')
    else:            #Spam
        return HttpResponse('spam')