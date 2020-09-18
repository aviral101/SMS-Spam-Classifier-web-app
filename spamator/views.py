from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from manage import importAlgo
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import string
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

# Create your views here.
def index(request):
    return render(request,'index.html')

def checksms(request):
    sms=request.POST.get('smstext','Guest')
    CV,NB = importAlgo()
    text = CV.transform([sms])
    result = NB.predict(text)
    context = {"Prediction":result}
    res=context["Prediction"]
    if res == 1:  #Ham
        return HttpResponse('ham')
    else:            #Spam
        return HttpResponse('spam')