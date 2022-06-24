from django.http import Http404
from django.shortcuts import redirect, render
from register.forms import TraineesForms

from register.models import Trainees
from .models import *
from .forms import *

# Create your views here.


def createTrainees(request):
    if request.method == 'POST':
        form = TraineesForms(request. POST)
        if form.is_valid():
            try:
                form.save()
                return redirect(listAllTrainees)
            except:
                pass
    else:
        form = TraineesForms()

    return render(request, "createTraineesForm.html", {'mmj': form})


def listAllTrainees(request):
    Train = Trainees.objects.all()
    return render(request, "listAllTraineesForm.html", {'trainees': Train})


def editTrainees(request, id):
    trainee = Trainees.objects.get(id=id)

    return render(request, "editTraineesform.html", {'trainer': trainee})


def updateTrainees(request, id):
    trainee = Trainees.objects.get(id=id)
    form = TraineesForms(request.POST, instance=trainee)
    if form.is_valid():
        form.save()
        return redirect('/listAllTrainees')

    return render(request, "updateTrainees.html", {'Enter': trainee})


def deleteTrainees(request, id):
    try:
        Trainees.objects.filter(id=id).delete()
    except Trainees.DoesNotExist:
        raise Http404("Trainee does not exist")
        return redirect(index)


def login(request):

    return render(request, "login.html")
