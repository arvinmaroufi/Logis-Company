from django.shortcuts import render
from .models import Project
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


def project_list(request):
    projects = Project.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(projects, 4)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)
    site_settings = SiteSettings.objects.first()
    services = Service.objects.all()
    context = {
        'projects': object_list,
        'pages_to_show': pages_to_show,
        'site_settings': site_settings,
        'services': services,
    }
    return render(request, 'project/project_list.html', context)

