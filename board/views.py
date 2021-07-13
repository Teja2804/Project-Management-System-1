from django.shortcuts import render
from django.http import HttpResponse

def board(request):
    return render(request, 'board.html')


 
