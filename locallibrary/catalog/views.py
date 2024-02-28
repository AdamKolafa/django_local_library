from django.shortcuts import render

# Create your views here.

from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # Calculate the count of genres
    num_genres = Genre.objects.count()

    # Calculate the count of books containing a particular word (case insensitive)
    word = request.GET.get('word', '')  # Get the word from the query string
    num_books_with_word = Book.objects.filter(title__icontains=word).count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_books_with_word': num_books_with_word,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    template_name = 'author_list.html'  # Define your author list template here
    context_object_name = 'author_list'

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'  # Define your author detail template here
    context_object_name = 'author'