from django.shortcuts import render

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

    context = {
        'num_books' : num_books,
        'num_instances' : num_instances,
        'num_instances_available' : num_instances_available,
        'num_authors' : num_authors,
        'count_e_genres' : count_e_genres,
        'count_o_authors' : count_o_authors,
    }

    return render(request, 'index.html', context)