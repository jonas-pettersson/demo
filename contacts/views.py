from django.shortcuts import render
from django.http import HttpResponse
from contacts.models import Contact, Company
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from rest_framework import viewsets, permissions
from .serializers import ContactSerializer, CompanySerializer


def index(request):
    contact_list = Contact.objects.all().order_by('last_name', 'first_name')
    context = {
        'contact_list': contact_list,
    }
    return render(request, 'contacts/contact_list.html', context)


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contacts/contact_detail.html'


class ContactUpdateView(UpdateView):
    model = Contact
    template_name = 'contacts/contact_form.html'
    fields = '__all__'


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('last_name', 'first_name')
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]
