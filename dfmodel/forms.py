from django import forms

class HomeForm(forms.Form):
    numTasks = forms.CharField(label='Number of Tasks', max_length=100)
    numFirms = forms.CharField(label='Number of Firms', max_length=100)

