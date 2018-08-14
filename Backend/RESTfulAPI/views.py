import json

from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.views import View

from RESTfulAPI.models import Picture
from utils import dictsub

# Create your views here.

class Search(View):
    def get(self, request):
        keyword = request.GET['keyword']
        pics = Picture.objects.filter(name__contains=keyword)

        response = [
            dictsub(model_to_dict(pic), ['name', 'source'])
            for pic in Picture.objects.filter(name__contains=keyword)
        ]
        return HttpResponse(json.dumps(response), content_type="application/json")
