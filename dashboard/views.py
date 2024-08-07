from django.shortcuts import render, redirect
from main import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        contacts = models.Contact.objects.all()
        counter = len(contacts)
        visible_contact = sum(1 for contact in contacts if contact.is_show==True)
        no_visible_c = counter - visible_contact
        context = {
            'contact':counter,
            'visible_counter':visible_contact,
            'no_visible':no_visible_c,
        }
    return render(request, 'dashboard/index.html', context)

def contactList(request):
    contacts = models.Contact.objects.all().order_by('is_show')
    return render(request, 'dashboard/contact.html', {'contacts':contacts})

def succes(request, id):
    obj = models.Contact.objects.get(id=id)
    obj.is_show = True
    obj.save()

    return redirect('contact')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    return render(request, 'dashboard/signin.html')

def log_out(request):
    logout(request)
    return redirect('index')

def banner(request):
    context = {}
    banners = models.Banner.objects.all()
    context['banners']=banners
    return render(request, 'dashboard/bannerlist.html', context)

def deletebanner(request, id):
    models.Banner.objects.get(id=id).delete()
    return redirect('banner')

def createbanner(request):
    if request.method == "POST":
        models.Banner.objects.create(
            title = request.POST['title'],
            sub_title = request.POST['sub_title'],
            body = request.POST['body']
        )
        return redirect('banner')
    return render(request, 'dashboard/createbanner.html')

def info(request):
    context = {}
    infos = models.Info.objects.all()
    context['infos']=infos
    return render(request, 'dashboard/infolist.html', context)

def deleteinfo(request, id):
    models.Info.objects.get(id=id).delete()
    return redirect('info')

def createinfo(request):
    if request.method == "POST":
        models.Info.objects.create(
            phone = request.POST['phone'],
            email = request.POST['email'],
            region = request.POST['region'],
            region_map = request.POST['region_map']
        )
        return redirect('info')
    return render(request, 'dashboard/createinfo.html')

def cell(request):
    context = {}
    cell = models.Cell.objects.all()
    context['cell']=cell
    return render(request, 'dashboard/celllist.html', context)

def deletecell(request, id):
    models.Cell.objects.get(id=id).delete()
    return redirect('cell')

def createcell(request):
    if request.method == "POST":
        models.Cell.objects.create(
            icon = request.POST['icon'],
            title = request.POST['title'],
            info = request.POST['info']
        )
        return redirect('cell')
    return render(request, 'dashboard/createcell.html')

def updatecell(request, id):
    context = {}
    cell = models.Cell.objects.get(id = id)
    context['cell'] = cell
    if request.method == 'POST':
        cell.icon = request.POST['icon']
        cell.title = request.POST['title']
        cell.info = request.POST['info']
        cell.save()
        return redirect('cell')
    return render(request, 'dashboard/createcell.html', context)
