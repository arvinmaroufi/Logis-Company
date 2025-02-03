from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactUsForm
from .models import SiteSettings, FAQ, Service, Comment


def home(request):
    site_settings = SiteSettings.objects.first()
    faq_list = FAQ.objects.all()
    services = Service.objects.all()
    comments = Comment.objects.all()[:5]
    context = {
        'site_settings': site_settings,
        'faq_list': faq_list,
        'services': services,
        'comments': comments,
    }
    return render(request, 'core/home.html', context)


def service_detail(request, slug):
    site_settings = SiteSettings.objects.first()
    service = get_object_or_404(Service, slug=slug)
    services = Service.objects.all()
    context = {
        'site_settings': site_settings,
        'service': service,
        'services': services,
        'current_service_slug': service.slug,
    }
    return render(request, 'core/service_detail.html', context)


def contact(request):
    site_settings = SiteSettings.objects.first()
    services = Service.objects.all()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = ContactUsForm()

    context = {
        'site_settings': site_settings,
        'services': services,
        'form': form
    }
    return render(request, 'core/contact.html', context)


