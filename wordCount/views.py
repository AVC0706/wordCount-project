import operator
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request , 'home.html'  )

def count(request):

    Text=request.GET['text']

    wlist=Text.split()
    wD={}

    for word in wlist:
        if word in wD:
            wD[word]+=1

        else:
            wD[word]= 1

    sortword = sorted(wD.items() , key=operator.itemgetter(1) , reverse=True)

    return render(request , 'count.html' , {'Text':Text , 'wlist':len(wlist) , 'wd': sortword }  )


def About(request):
    return render(request , 'about.html')
