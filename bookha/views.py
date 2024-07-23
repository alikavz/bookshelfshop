from django.urls import reverse_lazy
from django.views import generic
from .models import Book, Comment
from django.shortcuts import get_object_or_404, render
from .forms import Commentform
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class Booklis(generic.ListView):
    model = Book
    paginate_by = 2
    template_name = 'bookha/booklist.html'
    context_object_name = 'bookss'


# class Bookdetail(generic.DetailView):
#     model = Book
#     template_name = 'bookha/bookdetail.html'  #html akhar faramoosh nashavad

@login_required
def bookdetail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    comments1 = book.comments.all()
    if request.method == 'POST':
        comments2 = Commentform(request.POST)
        if comments2.is_valid():
            newcm = comments2.save(commit=False)
            newcm.Which_book = book
            newcm.user = request.user
            newcm.save()
            comments2 = Commentform()
    else:
        comments2 = Commentform()

    return render(request, 'bookha/bookdetail.html', {'book': book, 'comments': comments1, 'comment_form': comments2})


class Creating(LoginRequiredMixin, generic.CreateView):
    model = Book
    template_name = 'bookha/creating.html'
    fields = ['title', 'author', 'desc', 'price', 'covers']


class Updateview(LoginRequiredMixin, generic.UpdateView):
    model = Book
    template_name = 'bookha/updating.html'
    fields = ['title', 'author', 'desc', 'price', 'covers']


class Deleting(generic.DeleteView):
    model = Book
    template_name = 'bookha/deleting.html'
    success_url = reverse_lazy('booklis')

