from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance


#Inline classes 
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

class BookInline(admin.TabularInline):
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')] #purely to change on screen layout
    inlines=[BookInline]
    
#admin.site.register(Book)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Genre)
#admin.site.register(BookInstance)



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    """Administration object for BookInstance models.
    Defines:
     - fields to be displayed in list view (list_display)
     - filters that will be displayed in sidebar (list_filter)
     - grouping of fields into sections (fieldsets)
    """
    list_display = ('book', 'status','due_back', 'id','borrower')
    list_filter = ('status', 'due_back') #creates filter box to the right
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )
    
#@admin.register is equivalent too admin.site.register
#fieldsets just creates new dividers