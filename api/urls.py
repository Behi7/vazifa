# from django.urls import path
# from . import views

# urlpatterns = [
#     path('cell', views.cell, name='cell'),
#     path('info', views.info, name='info'),
#     path('banner', views.banner, name='banner'),
#     path('murojatlar', views.contactList, name='contact'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.ContactView.as_view()),
    path('contact/<int:pk>/', views.ContactObjView.as_view()),
    path('banner', views.BannerView.as_view()),
    path('banner/<int:pk>/', views.BannerObjView.as_view()),
    path('info', views.InfoView.as_view()),
    path('info/<int:pk>/', views.InfoObjView.as_view()),
    path('cell', views.CellView.as_view()),
    path('cell/<int:pk>/', views.CellObjView.as_view()),
]
