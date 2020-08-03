from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path(r'borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),  # Added for challenge
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
     path('author/<int:pk>',views.AuthorDetailView.as_view(), name='author-detail'),
]
#path(url pattern,view function, name to be used to reverse url)
#reverse url means  to dynamically create a URL that  points to the
# resource that the mapper is designed to handle.
#Example <a href="{% url 'index' %}">Home</a>.

#For Django class-based views we access an appropriate view function by calling the class method as_view()

#The syntax is very simple: angle brackets define the part of the 
# URL to be captured, enclosing the name of the variable that the 
# view can use to access the captured data. 
# For example, <something> , will capture the marked pattern 
# and pass the value to the view as a variable "something". 
# You can optionally precede the variable name with a 
# converter specification that defines the type of 
# data (int, str, slug, uuid, path).