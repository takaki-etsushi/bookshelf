from django.shortcuts import render
from django.views import generic
from .models import Shelf
from django.urls import reverse_lazy

class ListBookView(generic.ListView):
    template_name = 'book/book_list.html'
    model = Shelf
    context_object_name = 'Shelf'

class DetailBookView(generic.DetailView):
    template_name = 'book/book_detail.html'
    model = Shelf
    context_object_name = 'Shelf'
    
class CreateBookView(generic.CreateView):
    template_name = 'book/book_create.html'
    model = Shelf
    context_object_name = 'Shelf'
    fields = ('title', 'text', 'category')
    success_url = reverse_lazy('list-book')
    

class DeleteBookView(generic.DeleteView):
    template_name = 'book/book_confirm_delete.html'
    model = Shelf
    context_object_name = 'Shelf'
    success_url = reverse_lazy('list-book')
    

class UpdateBookView(generic.UpdateView):
    template_name = 'book/book_update.html'
    model = Shelf
    context_object_name = 'Shelf'
    fields = ('title', 'text', 'category')
    success_url = reverse_lazy('list-book')