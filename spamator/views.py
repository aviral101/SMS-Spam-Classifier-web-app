from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

# Create your views here.
def index(request):
    return render(request,'index.html')

def checksms(request):
    sms=request.POST.get('smstext','Guest')
    value = sms

    df = pd.read_csv('spam.csv', encoding="latin-1")
    df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
    df['label'] = df['v1'].map({'ham': 0, 'spam': 1})
    X = df['v2']
    y = df['label']
    cv = CountVectorizer()
    X = cv.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    clf = MultinomialNB()
    clf.fit(X_train, y_train)
    clf.score(X_test, y_test)
    y_pred = clf.predict(X_test)
    message = value
    data = [message]
    vect = cv.transform(data).toarray()
    res = clf.predict(vect)
    if res == 1:  #Ham
        return HttpResponse('spam')
    else:            #Spam
        return HttpResponse('ham')