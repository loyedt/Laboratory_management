from django.shortcuts import render
from django.http import HttpResponse
from .models import Tests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def tests(request):
    tsts =  Tests.objects.all()

    return render(request, 'tests.html',{'tsts': tsts})
