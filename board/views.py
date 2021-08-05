from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def project(request):

    Title = Board.objects.all()

    ThisBoard = InsideBoard.objects.all()

    form = CardForm()

    context = {'ThisBoard':ThisBoard, 'form':form, 'title':Title}

    return render(request, 'board.html',context)


def dashboard(request):

    Title = Board.objects.all()

    ThisBoard = InsideBoard.objects.all()

    form = CardForm()

    context = {'ThisBoard':ThisBoard, 'form':form, 'title':Title}

    return render(request, 'dashboard.html',context)

