from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Author, Book, BookInstance


def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available copies of books
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # The 'all()' is implied by default.

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors},
    )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

    # def get_context_data(self, **kwargs):
    #     # В первую очередь получаем базовую реализацию контекста
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     # Добавляем новую переменную к контексту и инициализируем её некоторым значением
    #     context['some_data'] = 'This is just some data'
    #     return context


class BookDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Book


def book_detail_view(request, pk):
    # try:
    #     book_id=Book.objects.get(pk=pk)
    # except Book.DoesNotExist:
    #     raise Http404("Book does not exist")

    book_id = get_object_or_404(Book, pk=pk)

    return render(
        request,
        'catalog/book_detail.html',
        context={'book': book_id, }
    )


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Author


def author_detail_view(request, pk):
    # try:
    #     book_id=Book.objects.get(pk=pk)
    # except Book.DoesNotExist:
    #     raise Http404("Book does not exist")

    author_id = get_object_or_404(Author, pk=pk)
    return render(
        request,
        'catalog/author_detail.html',
        context={'author': author_id, }
    )
