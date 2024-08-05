from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('murojatlar', views.contactList, name='contact'),
    path('murojat/see/<int:id>/', views.succes, name='see'),
    path('login', views.login_user, name='login'),
    path('log_out', views.log_out, name='log_out'),
    path('bannerlist', views.banner, name='banner'),
    path('deletebanner/<int:id>', views.deletebanner, name='deletebanner'),
    path('createbanner', views.createbanner, name='createbanner'),
    path('infolist', views.info, name='info'),
    path('deleteinfo/<int:id>/', views.deleteinfo, name ='deleteinfo'),
    path('createinfo', views.createinfo, name='createinfo'),
    path('infocell', views.cell, name='cell'),
    path('deletecell/<int:id>/', views.deletecell, name ='deletecell'),
    path('createcell', views.createcell, name='createcell'),
]