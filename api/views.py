from rest_framework import viewsets
from .serializers import ContactSerializer, BannerSerializer, InfoSerializer, CellSerializer, ContactObjSerializer
from main.models import Banner, Contact, Cell, Info
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics


class ContactObjView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactObjSerializer
    

class BannerObjView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class BannerView(generics.ListCreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

    
class InfoObjView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer


class InfoView(generics.ListCreateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer


class CellObjView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer


class CellView(generics.ListCreateAPIView):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer