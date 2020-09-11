from django.shortcuts import render
from django.http import HttpResponse
from contacts.models import Contact
from django.views.generic import DetailView


def index(request):
    contact_list = Contact.objects.all()
    context = {
        'contact_list': contact_list,
    }
    return render(request, 'contacts/contact_list.html', context)


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contacts/contact_detail.html'
