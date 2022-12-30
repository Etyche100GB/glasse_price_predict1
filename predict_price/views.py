from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
import joblib

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({},request))


def result(request):
    if request.method == 'POST':
        marque = int(request.POST['marque'])
        model = int(request.POST['modele'])
        taille = int(request.POST['taille'])
        couleur = int(request.POST['couleur'])
        
        
        predict = [[marque,model,taille,couleur]]

        regr = joblib.load('home_work_corr.pkl')
        rep = regr.predict(predict)
        print(rep)

        return HttpResponse('nice')




