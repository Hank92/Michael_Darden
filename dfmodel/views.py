import sys
import subprocess
import os
import boto3
import io

from django.shortcuts import render
from django.views.generic import TemplateView
from .cFile.differentialModel import *
from dfmodel.forms import HomeForm

# Create your views here.
class Home(TemplateView):
    def get(self, request):
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
    def get(self, request):
        s3 = boto3.resource('s3')
        bucket = s3.Bucket('dardendifferentialmodeloutput')
        file = []
        for obj in bucket.objects.all():
            key = obj.key
            body = obj.get()['Body']._raw_stream.readlines()
            temp = []
            temp.append(key)
            temp.append(body[0].decode("utf-8"))
            temp.append(body[1].decode("utf-8"))
            temp.append(body[2].decode("utf-8"))
            temp.append(body[3].decode("utf-8"))
            file.append(temp)
        result = {'output': file}
        return render(request, 'display.html', result)
    def post(self, request):
        #s3 = boto3.client('s3')
        #s3.download_file('dardendifferentialmodeloutput', request.POST["file"], "very Lovely")
        #print(request.POST["file"])
        success = "Your file has been downloaded!"
        args = {'success':success}
        return render(request, 'display.html', args)


