from .forms import BookForm
from .models import Book 
from django.shortcuts import render, get_object_or_404, redirect

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Z://books//quillcart//templates//quillcart//book_list.html')
    else:
        form = BookForm()
    return render(request, 'Z://books//quillcart//templates//quillcart//create_book.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'Z://books//quillcart//templates//quillcart//book_list.html', {'books': books})

def view_book(request, book_id):
    book = get_object_or_404(Book, custom_id=book_id)
    return render(request, 'Z://books//quillcart//templates//quillcart//view_book.html', {'book': book})

def update_book(request, book_id):
    book = get_object_or_404(Book, custom_id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = BookForm(instance=book)
    return render(request, 'Z://books//quillcart//templates//quillcart//update_book.html', {'form': form, 'book': book})

def delete_book(request, book_id):
    book = get_object_or_404(Book, custom_id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book-list')
    return render(request, 'Z://books//quillcart//templates//quillcart//delete_book.html', {'book': book})



