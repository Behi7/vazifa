from rest_framework import viewsets
from .serializers import ContactSerializer, BannerSerializer, InfoSerializer, CellSerializer
from main.models import Banner, Contact, Cell, Info

class ContactList(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class BannerList(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class InfoList(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer


class CellList(viewsets.ModelViewSet):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer
