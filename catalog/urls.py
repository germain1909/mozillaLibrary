from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
#path(url pattern,view function, name to be used to reverse url)
#reverse url means  to dynamically create a URL that  points to the
# resource that the mapper is designed to handle.
#Example <a href="{% url 'index' %}">Home</a>.