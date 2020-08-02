from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import *
from .models import *


# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))


class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('list_author')
    template_name = 'lib/add_author.html'


class AuthorRead(ListView):
    model = Author
    template_name = 'lib/list_authors.html'


class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('list_books')
    template_name = 'lib/add_book.html'


class BookRead(ListView):
    model = Book
    template_name = 'lib/list_books.html'


class DebtorCreate(CreateView):
    model = Debtor
    form_class = DebtorForm
    success_url = reverse_lazy('list_debtor')
    template_name = 'lib/add_debtor.html'


class DebtorRead(ListView):
    model = Debtor
    template_name = 'lib/list_debtors.html'


class PublishingHouseCreate(CreateView):
    model = PublishingHouse
    form_class = PublishingHouseForm
    success_url = reverse_lazy('list_pub_house')
    template_name = 'lib/add_pub_house.html'


class PublishingHouseRead(ListView):
    model = PublishingHouse
    template_name = 'lib/list_pub_house.html'
