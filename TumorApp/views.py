from django.shortcuts import render
from django.http import HttpResponse
import sklearn
import pickle
import joblib

# Create your views here.

def home(request):
    return render(request,'index.html')

def result(request):
    cls=joblib.load('final_model.sav')
 
    lis=[]
    lis.append(request.GET["Clump"])
    lis.append(request.GET["UnifSize"])
    lis.append(request.GET["UnifShape"])
    lis.append(request.GET["MargAdh"])
    lis.append(request.GET["SingEpiSize"])
    lis.append(request.GET["BareNuc"])
    lis.append(request.GET["BlandChrom"])
    lis.append(request.GET["NormNucl"])
    lis.append(request.GET["Mit"])
    ans=cls.predict([lis])
    
    return render(request,"result.html",{"ans":ans})
