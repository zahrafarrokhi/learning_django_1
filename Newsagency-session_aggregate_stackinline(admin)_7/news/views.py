import json
import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from .models import Article, Category, User, Author


@csrf_exempt
def show_articles(request):
     # print(dir(request))
    # print("request.POST: ", request.POST)
    # print("request.GET: ", query_url)
    # print("cookiie", request.COOKIES)
    # print(request.method)
    # print(cat)
    query_url = request.GET
    cat = query_url.get('cat', None)

    if cat:
        # cat = Category.objects.get( name=cat)
        cat = get_object_or_404(Category, name=cat)
        articles = cat.article_set.all()

    else:
        articles = Article.objects.all()  # QuerySet

    result = []
    for elm in articles:  
        result.append(
            {
                "title": elm.title,
                "author": elm.author.nick_name,
                "context": elm.context,
                "published": elm.date_pub,
                "slug": elm.slug
            }
        )

    return JsonResponse(result, safe=False)


def article_list(request):
    
    if request.method == 'GET':
        # query_set = Article.objects.all()
        # query_set = Article.objects.filter(
        #     title__startswith='hello') | Article.objects.filter(title__startswith='bye')

        query_set = Article.objects.prefetch_related('category').filter(
            date_pub__day__gt=datetime.datetime.today().day - 20).filter(title__startswith="hello")

        result = []
        for article in query_set:
            article_cats = []
            for cat_item in article.category.all():
                article_cats.append(cat_item.name)
            result.append({
                "title": article.title,
                "author": article.author.nick_name,
                "context": article.context,
                "published": article.date_pub,
                "path": article.get_absolute_url(),
                "cats": article_cats
            })
        return JsonResponse(result, safe=False)


def article_detail(request, slug=None):
    if request.method == 'GET':
        article = get_object_or_404(Article, slug=slug)
        result = {
            "title": article.title,
            "author": article.author.nick_name,
            "context": article.context,
            "published": article.date_pub,
        }

        print(request.session)
        request.session['name'] = 'ashkan'

        if not request.session.get('seen', None):
            request.session['seen'] = []
            request.session['seen'].append(article.slug)
            article.seen_num += 1
            article.save()
        elif article.slug not in request.session['seen']:
            request.session['seen'].append(article.slug)
            article.seen_num += 1
            article.save()

        
        return JsonResponse(result)
