from django.shortcuts import render
from .models import Project
from core.models import SiteSettings, Service


def project_list(request):
    site_settings = SiteSettings.objects.first()
    services = Service.objects.all()
    projects = Project.objects.all()
    context = {
        'site_settings': site_settings,
        'services': services,
        'projects': projects,
    }
    return render(request, 'project/project_list.html', context)

