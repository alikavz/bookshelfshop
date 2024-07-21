from django.views import generic
from .models import Book

class Booklis(generic.ListView):
    model = Book
    template_name = 'bookha/booklist'
    context_object_name = 'bookss'
