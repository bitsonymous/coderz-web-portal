from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Coders
from .forms import CoderForm

# Create your views here.
def index(request):
    return render(request,'coders/index.html', {
        'coders': Coders.objects.all()
    })
def view_coder(request,id):
    coder = Coders.objects.all(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = CoderForm(request.POST)
        if form.is_valid():
            new_coder_number = form.cleaned_data['coder_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_lc_id = form.cleaned_data['lc_id']
            new_rating = form.cleaned_data['rating']

            new_coder= Coders(
                coder_number = new_coder_number,
                first_name = new_first_name ,
                last_name = new_last_name,
                lc_id = new_lc_id ,
                rating = new_rating,
            )
            new_coder.save()
            return render(request,'coders/add.html', {
                'form': CoderForm(),
                'success': True
            })
    else:
        form = CoderForm()
    return render(request,'coders/add.html', {
            'form': CoderForm()
    })

def edit(request, id):
    if request.method == 'POST':
        coder = Coders.objects.get(pk=id)
        form = CoderForm(request.POST, instance=coder)
        if form.is_valid():
            form.save()
            return render(request,'coders/edit.html', {
                'form': form,
                'success': True
            })
    else:
        coder = Coders.objects.get(pk=id)
        form = CoderForm(instance=coder)
    return render(request,'coders/edit.html', {
        'form': form
    })

def delete(request, id):
    if request.method == 'POST':
        coder = Coders.objects.get(pk=id)
        coder.delete()
    return HttpResponseRedirect(reverse('index'))

