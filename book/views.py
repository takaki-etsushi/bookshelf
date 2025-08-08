from django.shortcuts import render
from django.views import generic
from .models import Shelf, Review
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

class ListBookView(generic.ListView):
    template_name = 'book/book_list.html'
    model = Shelf
    context_object_name = 'Shelf'

class DetailBookView(generic.DetailView):
    template_name = 'book/book_detail.html'
    model = Shelf
    context_object_name = 'Shelf'
    
class CreateBookView(LoginRequiredMixin, generic.CreateView):
    template_name = 'book/book_create.html'
    model = Shelf
    context_object_name = 'Shelf'
    fields = ('title', 'text', 'category', 'thumbnail')
    success_url = reverse_lazy('list-book')
    
    def form_valid(self, form):
        form.instance.user = self.request.user  # ログイン中のユーザーを設定
        return super().form_valid(form)
    

class DeleteBookView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'book/book_confirm_delete.html'
    model = Shelf
    context_object_name = 'Shelf'
    success_url = reverse_lazy('list-book')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied('削除権限がありません。')
        return super(DeleteBookView, self).dispatch(request, *args, **kwargs)


class UpdateBookView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'book/book_update.html'
    model = Shelf
    context_object_name = 'Shelf'
    fields = ('title', 'text', 'category', 'thumbnail')
    success_url = reverse_lazy('list-book')
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied('編集権限がありません。')
        return super(UpdateBookView, self).dispatch(request, *args, **kwargs)
    

class CreateReviewView(LoginRequiredMixin, generic.CreateView):
    model = Review
    fields = ('book', 'title', 'text', 'rate')
    template_name = 'book/review_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = Shelf.objects.get(pk=self.kwargs['book_id'])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail-book', kwargs={'pk':self.object.book.id})