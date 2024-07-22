from django.urls import reverse_lazy
from django.views import generic
from .models import Book, Comment
from django.shortcuts import get_object_or_404, render


class Booklis(generic.ListView):
    model = Book
    paginate_by = 2
    template_name = 'bookha/booklist.html'
    context_object_name = 'bookss'


# class Bookdetail(generic.DetailView):
#     model = Book
#     template_name = 'bookha/bookdetail.html'  #html akhar faramoosh nashavad

def bookdetail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    comments = book.comments.all()
    return render(request, 'bookha/bookdetail.html', {'book': book, 'comments': comments})


class Creating(generic.CreateView):
    model = Book
    template_name = 'bookha/creating.html'
    fields = ['title', 'author', 'desc', 'price', 'covers']


class Updateview(generic.UpdateView):
    model = Book
    template_name = 'bookha/updating.html'
    fields = ['title', 'author', 'desc', 'price', 'covers']


class Deleting(generic.DeleteView):
    model = Book
    template_name = 'bookha/deleting.html'
    success_url = reverse_lazy('booklis')

