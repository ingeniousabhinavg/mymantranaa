from multiprocessing import context
from django.shortcuts import render
from .models import *

# call your data from models

servicesData = Services.objects.all()
counsellorsData = Counsellors.objects.all()

context = {
    'services':servicesData,
    'counsellors':counsellorsData,
}

# Create your views here.
def index(request):
    return render(request, 'index.html', context)