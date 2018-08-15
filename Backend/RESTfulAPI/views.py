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

        # 按照名字查找, 返回结果携带tags
        response = []
        for pic in pics:
            tags = [tag['name'] for tag in pic.tags.values()]

            pic_info = dictsub(model_to_dict(pic), ['name', 'source'])
            pic_info['tags'] = tags
            response.append(pic_info)

        return HttpResponse(json.dumps(response), content_type="application/json")
