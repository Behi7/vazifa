from django.shortcuts import render, redirect
from . import models

def index(request):
    banner = models.Banner.objects.last()
    info = models.Info.objects.last()
    cell = models.Cell.objects.all()
    link = models.Link.objects.last()
    context = {
        'banner':banner,
        'info':info,
        'cell':cell,
        'link':link,
    }
    return render(request, 'main/index.html', context)


def contactCreate(request):
    if request.method == 'POST':
        models.Contact.objects.create(
            full_name = request.POST['name'],
            phone = request.POST['phone'],
            subject = request.POST['subject'],
            text = request.POST['text']
        )
    return redirect('index')