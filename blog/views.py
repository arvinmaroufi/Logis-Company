from django.shortcuts import render, get_object_or_404
from .models import Article
from core.models import SiteSettings, Service
from django.core.paginator import Paginator


def get_pages_to_show(current_page, total_pages):
    if total_pages <= 3:
        return list(range(1, total_pages + 1))

    if current_page <= 2:
        return [1, 2, 3, '...', total_pages]

    if current_page >= total_pages - 1:
        return [1, '...', total_pages - 2, total_pages - 1, total_pages]

    return [1, '...', current_page - 1, current_page, current_page + 1, '...', total_pages]


def article_list(request):
    articles = Article.objects.filter(status='published')
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 6)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)
    site_settings = SiteSettings.objects.first()
    services = Service.objects.all()
    context = {
        'articles': object_list,
        'pages_to_show': pages_to_show,
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

