from django.shortcuts import render,redirect
from . import forms
from . import models

# Create your views here.
def add_categories(request):
    if request.method=='POST':
        category_form = forms.CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect(add_categories)
    else:
        category_form = forms.CategoryForm()
        return render(request,'add_catagories.html',{'form': category_form})