from django.shortcuts import render, redirect
from .forms.EmployeForm import EmployeForm
from .models import Employe
import os
from .mock import create_some_employees
from django.core.paginator import Paginator

# Create your views here.

def list_employe(request):
    if len(Employe.objects.all()) == 0:
        create_some_employees()
    employes = Employe.objects.get_queryset().order_by('id')
    paginator = Paginator(employes, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'employe/list_employe.html', locals())

def add_employe(request):
    employe_form = EmployeForm()
    if request.method == 'POST':
        employe_form = EmployeForm(request.POST, request.FILES)
        if employe_form.is_valid():
            employe_form.save()
            return redirect('list_employe')
    return render(request, 'employe/add_employe.html', locals())

def remove_employe(request, id):
    employe = Employe.objects.get(id=id)
    os.remove(employe.photo_de_profil.path)
    employe.delete()
    return redirect('list_employe')

def details_employe(request, id):
    employe = Employe.objects.get(id=id)
    return render(request, 'employe/details.html', locals())
