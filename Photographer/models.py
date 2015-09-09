from django.db import models
from django import forms
from froala_editor.fields import FroalaField

class Test(models.Model):
    title = forms.CharField(max_length=100)
    image = forms.ImageField()
    froala = FroalaField()
