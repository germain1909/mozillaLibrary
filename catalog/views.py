from django.shortcuts import render
from django.views import generic

# Create your views here.

from catalog.models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    #filter has differnt __match methods
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    #Render method render(request object,html template with placeholders for data, context which is a python dictionary with the data for the template)
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'  # Specify your own template name/location
    paginate_by = 4

    
#The generic view will query the database to get all records for the 
# specified model (Book) then render a template 
# located at /locallibrary/catalog/templates/catalog/book_list.html 
# (which we will create below). Within the template you can access the
# list of books with the template variable name object_list OR book_list (
# i.e. generically "the_model_name_list").

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'  # Specify your own template name/location
    
#aboce looks for template book_detail because takes the model name and adds _detail