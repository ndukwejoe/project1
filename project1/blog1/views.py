from django.shortcuts import render
from .models import Board

# Create your views here.
def index(request):
    context={
    'board':Board.objects.all()
    }
    return render(request,'blog1/index.html',context)
