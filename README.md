## RealDelicious

真香！表情包存储搜索系统！

## Demo

[真香Demo](http://www.shaonianxiaoqi.com:8000)

## 依赖

1. python3
2. nodejs && npm
3. tesseract

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

2018.08.16 做了根据tag名多词搜索，图片从本地的自动导入。下一步更新前端。

2018.08.18 完善前端。修复搜索bug。项目Demo部署到云端。
