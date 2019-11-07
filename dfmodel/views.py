import sys
import subprocess
import os

from django.shortcuts import render
from django.views.generic import TemplateView
from .cFile.differentialModel import *

from dfmodel.forms import HomeForm

# Create your views here.
class Home(TemplateView):
    def get(self, request):
        #temp = dfModel()
        form = HomeForm()
        return render(request, 'index.html', {'form': form})
    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            numTasks = form.cleaned_data['numTasks']
            numFirms = form.cleaned_data['numFirms']
            temp = dfModel(numTasks, numFirms)
        success = "Computation successful with num task equal to " + numTasks + " and number of firms equal to " + numFirms
        args = {'form':form, 'success':success}
        return render(request, temp, args)

class Display(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'display.html', context=None)



