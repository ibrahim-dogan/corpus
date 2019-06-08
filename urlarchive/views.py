from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Category, URL


# Create your views here.
def urls(request):
    context = {
        'categories': Category.objects.all().reverse(),
    }

    return render(request, 'urlarchive/index.html', context)


@login_required
def new_url(request):
    title = request.POST.get('title')
    website = request.POST.get('website')
    category = request.POST.get('category')
    description = request.POST.get('description')

    url = URL(title=title, website=website, category=Category.objects.get(title=category), description=description)
    url.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def new_cat(request):
    title = request.POST.get('title')
    icon = request.POST.get('icon')

    category = Category(title=title, icon=icon)
    category.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
