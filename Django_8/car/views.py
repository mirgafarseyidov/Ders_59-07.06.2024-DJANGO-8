from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.



def sahib_detail_view(request, id):
    sahib=get_object_or_404(Sahib, id=id)
    
    
    return render(request, 'sahib_detal.html', {"sahib":sahib})

def galeri_detail_view(request, id):
    galeriya=get_object_or_404(Galeriya, id=id)
    masinlar=Masin.objects.filter(galeriya=galeriya)
    
    context = {
        'galeriya':galeriya,
        'masinlar':masinlar
    }
    
    return render(request, 'galeri_detal.html', {"galeriya":galeriya})
