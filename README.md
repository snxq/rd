## RealDelicious

真香！表情包存储搜索系统！


## 运行

前端构建
```
cd Frontend
npm install
npm run build
```

后端构建
```
pip install -r requirements.txt
cd Backend
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## 计划

1. 搜索
2. 图片管理（包括上传、手动打标签）
3. 图片自动打标签

## 进度

2018.08.14 目前做了简单的demo，连接了前后端。下一步做图片的搜索。
2018.08.15 做了根据名字的单keyword搜索。下一步做根据tag名的多keyword搜索。
