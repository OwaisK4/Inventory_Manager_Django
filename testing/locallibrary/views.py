from django.shortcuts import render
from django.views import generic

# Create your views here.
from .models import Book, Genre, Author, BookInstance

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.all().count()

    count_e_genres = Genre.objects.filter(name__icontains='e').count()
    count_o_authors = Author.objects.filter(first_name__icontains='o').count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books' : num_books,
        'num_instances' : num_instances,
        'num_instances_available' : num_instances_available,
        'num_authors' : num_authors,
        'count_e_genres' : count_e_genres,
        'count_o_authors' : count_o_authors,
        'num_visits' : num_visits,
    }

    return render(request, 'index.html', context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    context_object_name = 'book_list'
    # queryset = Book.objects.filter(title__icontains='war')[:5]
    queryset = Book.objects.all()

    def get_queryset(self):
        # return Book.objects.filter(title__icontains='war')[:5]
        return Book.objects.all()
    
    # def get_context_data(self, **kwargs):
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     context['some_data'] = 'This is just some data'
    #     return context

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'

class AuthorDetailView(generic.DetailView):
    model = Author