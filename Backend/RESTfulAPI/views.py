import json

import jieba
import pytesseract
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.views import View
from PIL import Image

from RESTfulAPI.models import Picture
from utils import dictsub

import jieba
from scipy.spatial.distance import sqeuclidean
# Create your views here.


class Search(View):
    """Search API"""
    def get(self, request):
        """search逻辑
        """
        def serializer(queryset):
            """序列化"""
            response = []
            for pic in queryset[:-1]:
                pic_info = dictsub(model_to_dict(pic[0]), ['name', 'source', 'description'])
                pic_info['tags'] = pic[2]
                response.append(pic_info)

            return json.dumps(response)

        # 参数处理
        keywords = request.GET['keywords']
        limit = max(int(request.GET['limit']), 100)
        offset = int(request.GET['offset'])
        words = list(jieba.cut_for_search(keywords))

        # 数据库Query
        query = Picture.objects.all()

        # 计算相似度 对结果排序
        response = [(-1, -1, -1)]
        for pic in query:
            tags = [tag['name'] for tag in pic.tags.values()]
            # 重复的元素数量/总数量+1
            distance = (len(tags+words)-len(set(tags+words)))/(len(set(tags+words))+1)
            # distance = sqeuclidean(words, tags)
            temp = [] + response
            for index, item in enumerate(temp):
                # import pdb; pdb.set_trace()
                if distance > item[1]:
                    response.insert(index, (pic, distance, tags))

        return HttpResponse(
            serializer(response[limit*offset:limit*offset+limit]),
            content_type="application/json"
        )
