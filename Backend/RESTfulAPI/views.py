# coding: utf-8
"""RESTful API
1. Search 图片的搜索
"""

import json
import random

import jieba
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.views import View

from RESTfulAPI.models import Picture
from utils import dictsub

# Create your views here.


class Search(View):
    """Search API"""
    def get(self, request):
        """search逻辑
        """
        def serializer(queryset):
            """序列化"""
            response = []
            for pic in queryset:
                pic_info = dictsub(model_to_dict(pic[0]), ['name', 'source', 'description'])
                pic_info['tags'] = pic[2]
                response.append(pic_info)

            return json.dumps(response)

        # 参数处理
        keywords = request.GET['keywords']
        limit = int(request.GET['limit']) if int(request.GET['limit']) < 100 else 100
        offset = int(request.GET['offset'])
        words = list(jieba.cut_for_search(keywords))
        words_length = len(words)

        # 数据库Query
        query = Picture.objects.all()

        # 计算相似度 对结果排序
        response = []
        zero_distance = []
        for pic in query:
            tags = [tag['name'] for tag in pic.tags.values()]
            tags_length = len(tags)
            total_length = len(set(tags+words))

            # 重复的元素数量/总数量+1
            distance = (tags_length+words_length-total_length)/(total_length+1)

            # distance == 0 两种情况 1. 没有tags 2. 有但没有重复
            if distance == 0:
                zero_distance.append((pic, 0, tags))
                continue

            if not response:
                response.append((pic, distance, tags))
                continue

            temp = [] + response
            for index, item in enumerate(temp):
                if distance > item[1]:
                    response.insert(index, (pic, distance, tags))
                    break

        if len(response) < limit:
            random.shuffle(zero_distance)
            response += zero_distance[:limit - len(response)]

        return HttpResponse(
            serializer(response[limit*offset:limit*offset+limit]),
            content_type="application/json"
        )
