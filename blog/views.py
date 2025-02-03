from django.shortcuts import render, get_object_or_404
from .models import Article
from core.models import SiteSettings, Service


def article_list(request):
    articles = Article.objects.filter(status='published')
    site_settings = SiteSettings.objects.first()
    services = Service.objects.all()
    context = {
        'articles': articles,
        'site_settings': site_settings,
        'services': services,
    }
    return render(request, 'blog/article_list.html', context)


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    latest_articles = Article.objects.filter(status='published').exclude(slug=article.slug).order_by('-created_at')[:3]
    site_settings = SiteSettings.objects.first()
    services = Service.objects.all()
    context = {
        'article': article,
        'latest_articles': latest_articles,
        'site_settings': site_settings,
        'services': services,
    }
    return render(request, 'blog/article_detail.html', context)

