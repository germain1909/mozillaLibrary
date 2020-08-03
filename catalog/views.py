from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from catalog.forms import RenewBookForm
import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from catalog.models import Author

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

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    #Here we first get the value of the 'num_visits' session key, setting the 
    # value to 0 if it has not previously been set. Each time a request is received, 
    # we then increment the value and store it back in the 
    # session (for the next time the user visits the page). 
    # The num_visits variable is then passed to the template in our context variable.

    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
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



class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name ='bookinstance_list_borrowed_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

        #LoginRequiredMixin means only logged in users can call this view

#class LoanedBooksAllListView(PermissionRequiredMixin, generic.ListView):
#come back and add permissions
class LoanedBooksAllListView(generic.ListView):
    """Generic class-based view listing all books on loan. Only visible to users with can_mark_returned permission."""
    model = BookInstance
    #permission_required = 'catalog.can_mark_returned'
    #come back and finish permissions
    template_name = 'bookinstance_list_borrowed_all.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')

def renew_book_librarian(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed') )

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'book_renew_librarian.html', context)

class AuthorCreate(CreateView):
    model = Author
    template_name = 'author_form.html'
    fields = '__all__'
    initial = {'date_of_death': '05/01/2018'}

class AuthorUpdate(UpdateView):
    model = Author
    template_name = 'author_form.html'
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    context = {
        
    }

class AuthorDelete(DeleteView):
    model = Author
    template_name = 'author_confirm_delete.html'
    success_url = reverse_lazy('authors')

class AuthorDetailView(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = Author
    template_name = 'author_detail.html'
