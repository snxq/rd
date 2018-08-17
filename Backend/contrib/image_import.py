# coding: utf-8
"""
图片导入
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RealDelicious.settings')
import django
django.setup()
import jieba
from django.db import transaction

# import pdb; pdb.set_trace()
from RESTfulAPI.models import Picture, Tag
from utils import ocr_extract_word

SOURCE = 'https://raw.githubusercontent.com/yodark1995/PictureNetworkStorage/master/resource/RealDelicious/'
def image_import(path):
    """ 图片批量导入
    """
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.split('.')[-1] not in ['jpeg', 'png', 'jpg']:
                continue
            image = os.path.join(dirpath, filename)

            # 图片识别
            out = ocr_extract_word(image)
            words = set(jieba.cut_for_search(out))

            print(filename, out, words)

            # 创建Obj
            with transaction.atomic():
                # 结巴分词
                tags = [Tag.objects.get_or_create(name=tag)[0] for tag in words if words]
                pic, _ = Picture.objects.get_or_create(name=filename)
                pic.description = out
                pic.tags.set(tags)
                pic.source = SOURCE + filename
                pic.save()
