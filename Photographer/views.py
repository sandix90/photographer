from django.shortcuts import render_to_response
from Photographer.models import Test

def index(request):
    objects = Test.objects.all()

    return render_to_response('Photographer\index.html', {'objects': objects})

