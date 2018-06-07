from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import dashview

@login_required(login_url="/home/login/")
def index(request):
    dashboard = dashview.objects.all()[:10]

    context = {
        'dashboard':dashboard
    }
    return render(request, 'index.html', context)
# Create your views here.
#def dashboard(request):
    #return HttpResponse('this is the dashboard')
@login_required(login_url="/home/login/")
def details(request, id):
    dashboard = dashview.objects.get(id=id)

    context = {
        'dashview':dashview
    }
    return render(request, 'details.html', context)
