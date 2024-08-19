from django.shortcuts import render

rooms = [
    {'id':1, 'name':'lets learn python!'},
    {'id':2, 'name':'lets learn django!'},
    {'id':3, 'name':'lets learn flask!'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html')

def room(request, pk):
    return render(request, 'base/room.html')
