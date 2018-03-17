# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import forms
from . import test

# Create your views here.

def index(request):
    return render(request, 'newapp/index.html')

def form_name_view(request):
    form = forms.Formname()
    #form = {"name":"sunil", "age":20}
    #form = [10, 30, 55]
    if request.method == 'POST':
        form = forms.Formname(request.POST)
        if form.is_valid():
            print test.name
            print "Success!"
            print form.data['email']
    return render(request, 'newapp/form_page.html', {'form':form})
