from django.shortcuts import render, redirect
from .forms import UrlForm
from .models import Url
from django.http import HttpResponse


def home(request):
    urls = Url.objects.all()

    return render(request, 'urlapp/home.html', {"urls": urls})

def add_url(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UrlForm()

    return render(request, 'urlapp/add_url.html', {'form': form})


def url(request, url):
    short_urls = []

    for i in Url.objects.all():
        short_urls.append(i.short_url)

    if url in short_urls:
        urla = Url.objects.get(short_url=url)
        long_url = urla.long_url
        url_name = urla.name
        urla.click_count += 1
        urla.save()
        return render(request, 'urlapp/url.html', {"short_url": url, 'long_url': long_url, "url_name": url_name, "click_count": urla.click_count})
    else:
        return render(request, 'urlapp/error.html')

def delete(request, url):
    url = Url.objects.get(short_url=url)
    if request.method == 'POST':
        url.delete()
        return redirect("/")
    else:
        return render(request, 'urlapp/home.html')

