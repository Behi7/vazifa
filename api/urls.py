# from django.urls import path
# from . import views

# urlpatterns = [
#     path('cell', views.cell, name='cell'),
#     path('info', views.info, name='info'),
#     path('banner', views.banner, name='banner'),
#     path('murojatlar', views.contactList, name='contact'),
# ]
from django.urls import path
from .views import ContactList, BannerList, InfoList, CellList, ContactDetail, BannerDetail, InfoDetail, CellDetail

urlpatterns = [
    path('contacts/', ContactList.as_view({'get': 'list'})),
    path('banners/', BannerList.as_view({'get': 'list'})),
    path('info/', InfoList.as_view({'get': 'list'})),
    path('cell/', CellList.as_view({'get': 'list'})),
    path('contacts/<int:pk>', ContactDetail.as_view()),
    path('banners/<int:pk>', BannerDetail.as_view()),
    path('info/<int:pk>', InfoDetail.as_view()),
    path('cell/<int:pk>', CellDetail.as_view())
]
