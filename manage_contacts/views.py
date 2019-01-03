from django.http import HttpResponseRedirect, request
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Person, Contact


class IndexView(generic.ListView):
    template_name = 'manage_contacts/index.html'
    context_object_name = 'person_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Person.objects.order_by('pk')


class DetailView(generic.DetailView):
    model = Person
    template_name = 'manage_contacts/detail.html'


class AddPersonView(generic.CreateView):
    model = Person
    fields = ['name', 'profile_picture']
    template_name = 'manage_contacts/add_person.html'

class AddContactView(generic.CreateView):
    model = Contact
    fields = ['name', 'address', 'phone', 'person']
    template_name = 'manage_contacts/add_contact.html'


def add_person(request):
    try:
        person = Person(name=request.POST['name'], profile_picture=request.POST['profile_picture'])
        person.save()
    except KeyError:
        return render(request, 'manage_contacts/add_person.html', {
            'error_message': "There was an error."})
    else:
        return HttpResponseRedirect(reverse('manage_contacts:detail', args=(person.id,)))

def add_contact(request):
    try:
        contact = Contact(name=request.POST['name'], address=request.POST['address'], phone=request.POST['phone'],person=request.POST['person'])
        contact.save()
    except KeyError:
        return render(request, 'manage_contacts/add_contact.html', {
            'error_message': "There was an error."})
    else:
        return HttpResponseRedirect(reverse('manage_contacts:detail', args=(contact.person_set[:1].id,)))
