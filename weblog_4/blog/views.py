from django.shortcuts import get_object_or_404, render
from .models import Article
# Create your views here.

def all_articles(request):
    # all_articles = Article.objects.all()
    # all_articles = Article.objects.filter(status ='puplish')
	
	# manager
    all_articles = Article.puplished.all()
    context ={'all_articles':all_articles}
    return render (request,'blog/all_articles.html',context)


def article_detail_id(request, id):
	article = get_object_or_404(Article, id=id)
	return render(request, 'blog/article.html', {'article':article})

def article_detail(request, slug):
	article = get_object_or_404(Article, slug=slug)
	return render(request, 'blog/article.html', {'article':article})


def article_details(request,id, slug):
	article = get_object_or_404(Article,id=id , slug=slug)
	return render(request, 'blog/article.html', {'article':article})