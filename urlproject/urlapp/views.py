from django.shortcuts import render, redirect
from .forms import UrlForm


def home(request):
    return render(request, 'urlapp/home.html')

def add_url(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UrlForm()

    return render(request, 'urlapp/add_url.html', {'form': form})