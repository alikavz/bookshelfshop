from django.views import generic
from .models import Book

class Booklis(generic.ListView):
    model = Book
    template_name = 'bookha/booklist.html'
    context_object_name = 'bookss'


class Bookdetail(generic.DetailView):
    model = Book
    template_name = 'bookha/bookdetail.html'  #html akhar faramoosh nashavad

