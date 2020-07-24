from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
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