from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Menu

# Create your views here.
def index_view(request):
    context = dict()
    today = str(datetime.now().date())
    context["today"] = today
    menus = Menu.objects.all()
    context["menus"] = menus
    return render(request, 'menus/index.html', context=context)

def detail(request, pk):
    menu = Menu.objects.get(id=pk)
    return render(request, 'menus/detail.html', {'menu':menu})