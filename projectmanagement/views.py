from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    # return HttpResponse('{% homepage.html %}')
    return render(request, 'homepage.html')


def board(request):
    return render(request, 'board.html')

def add_card(request):
    return render(request, 'card.html')