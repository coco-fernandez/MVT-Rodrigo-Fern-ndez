from django.shortcuts import render
from .models import Familiares


def index(request):
    familiares=Familiares.objects.all()
    ctx={'familiares':familiares}
    return render(request,"familiaresapp/index.html",ctx)
