from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def board(request):

    ThisBoard = InsideBoard.objects.all()

    form = CardForm()

    context = {'ThisBoard':ThisBoard, 'form':form}

    return render(request, 'board.html',context)


 