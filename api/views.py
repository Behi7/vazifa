from rest_framework import viewsets
from .serializers import ContactSerializer, BannerSerializer, InfoSerializer, CellSerializer
from main.models import Banner, Contact, Cell, Info
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ContactList(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetail(APIView):
    def get(self, request, pk):
        contact = Contact.objects.get(pk=pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)


class BannerList(viewsets.ModelViewSet): 
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class BannerDetail(APIView):
    def get(self, request, pk):
        contact = Banner.objects.get(pk=pk)
        serializer = BannerSerializer(contact)
        return Response(serializer.data)


class InfoList(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer


class InfoDetail(APIView):
    def get(self, request, pk):
        contact = Info.objects.get(pk=pk)
        serializer = InfoSerializer(contact)
        return Response(serializer.data)


class CellList(viewsets.ModelViewSet):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer


class CellDetail(APIView):
    def get(self, request, pk):
        contact = Cell.objects.get(pk=pk)
        serializer = CellSerializer(contact)
        return Response(serializer.data)