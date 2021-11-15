from django.shortcuts import render, redirect
from .models import Books
from .form import BookCreate
from django.http import HttpResponse
# Create your views here.


# home page, read and render all data from database (read)
def index(request):
    bookShelf = Books.objects.all()
    # send data "bookShelf" into library.html to render
    return render(request, 'library/library.html', {'bookShelf': bookShelf})


# add new data into data base in uploadForm page (create)
def upload(request):
    newBook = BookCreate()
    if request.method == 'POST':
        # request.FILES is for the image field
        newBook = BookCreate(request.POST, request.FILES)
        if newBook.is_valid():
            newBook.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload <a href = "{{ url : 'index'}}">here</a>""")
    else:
        # send form "newBook" into uploadForm.html to render
        return render(request, 'library/uploadForm.html', {'uploadForm': newBook})


# update data corresponding to the id (update)
def update(request, bookId):
    bookId = int(bookId)
    try:
        selectedBook = Books.objects.get(id=bookId)
    except Books.DoesNotExist:
        return redirect('index')
    # instance=selectedBook is to return the form filled with data coresponding to the id id
    editedBook = BookCreate(request.POST or None, instance=selectedBook)
    if editedBook.is_valid():
        editedBook.save()
        return redirect('index')
    return render(request, 'library/uploadForm.html', {'uploadForm': editedBook})


# delete data corresponding to the id (delete)
def delete(request, bookId):
    bookId = int(bookId)
    try:
        selectedBook = Books.objects.get(id=bookId)
    except Books.DoesNotExist:
        return redirect('index')
    selectedBook.delete()
    return redirect('index')
