import json
import os

import uuid
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index_page(req):
    pin_articles = models.Article.objects.filter(status=1, pin=1).order_by('-time')
    recent_articles = models.Article.objects.filter(status=1).order_by('-time')[:5]
    categories = models.Category.objects.all()
    tags = models.Tag.objects.all()
    context = {
        'pin_articles': pin_articles,
        'recent_articles': recent_articles,
        'categories': categories,
        'tags': tags,
    }
    return render(req, 'blog/index.html', context=context)


def article_list(req):
    category = req.GET.get('category', None)
    tag = req.GET.get('tag', None)
    page = req.GET.get('page', '1')
    filter_string = ''
    if category:
        articles = models.Article.objects.filter(status=1, category=int(category)).order_by('-time')
        filter_string = 'category=' + category
    elif tag:
        articles = models.Article.objects.filter(status=1, tags=int(tag)).order_by('-time')
        filter_string = 'tag=' + tag
    else:
        articles = models.Article.objects.filter(status=1).order_by('-time')
    paginator = Paginator(articles, 10)  # 每页 10 篇文章
    try:
        ok_articles = paginator.page(int(page))
    except:
        ok_articles = paginator.page(1)
    context = {
        'articles': ok_articles,
        'filter_string': filter_string,
    }
    return render(req, 'blog/article_list.html', context=context)


def article_detail(req, article_id):
    article = models.Article.objects.filter(id=int(article_id))[0]
    context = {
        'article': article,
    }
    return render(req, 'blog/article_detail.html', context=context)


def category_list(req):
    categories = models.Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(req, 'blog/category_list.html', context=context)


def tag_list(req):
    tags = models.Tag.objects.all()
    context = {
        'tags': tags,
    }
    return render(req, 'blog/tag_list.html', context=context)


def about_page(req):
    return render(req, 'blog/about.html')


@login_required(login_url='/manager/login/')
def admin_edit_article(req):
    article_id = req.GET['id']
    article = models.Article.objects.filter(id=int(article_id))
    if len(article) != 1:
        return HttpResponse('参数错误，未找到这篇文章。')
    article = article[0]
    context = {
        'article': article
    }
    return render(req, 'blog/admin/editor.html', context=context)


@csrf_exempt
@login_required(login_url='/manager/login/')
def admin_edit_save(req):
    data = req.POST.get('editormd-markdown-doc', None)
    article_id = req.POST.get('id', None)
    if id and data:
        article = models.Article.objects.filter(id=int(article_id))
        if len(article) == 1:
            article = article[0]
            article.text = data
            article.save()
            msg = '保存成功。'
        else:
            msg = '文章id错误，保存失败。'
    else:
        msg = '数据格式错误，保存失败。'
    result = {
        'status': msg,
    }
    return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_exempt
@login_required(login_url='/manager/login/')
def admin_image_upload(req):
    data = req.FILES.get('editormd-image-file', None)
    if data:
        extension = os.path.splitext(data.name)[-1]
        file_name = str(uuid.uuid1())
        with open(os.path.join(settings.BASE_DIR, 'uploads', 'images', file_name) + extension, 'wb+') as destination:
            for chunk in data.chunks():
                destination.write(chunk)
        result = {
            'success': 1,
            'message': '上传成功。',
            'url': '/uploads/images/' + file_name + extension,
        }
    else:
        result = {
            'success': 0,
            'message': '上传失败，请重试。',
            'url': '/',
        }
    return HttpResponse(json.dumps(result), content_type='application/json')
