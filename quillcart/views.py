from .forms import BookForm
from .models import Book 
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quillcart//book_list.html')
    else:
        form = BookForm()
    return render(request, 'quillcart//create_book.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 10)  # Show 10 books per page

    page_number = request.GET.get('page')
    
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # If the page is not an integer, show the first page
        page = paginator.page(1)
    except EmptyPage:
        # If the page is out of range (e.g., 9999), deliver the last page
        page = paginator.page(paginator.num_pages)

    return render(request, 'quillcart/book_list.html', {'books': page})

def view_book(request, book_id):
    book = get_object_or_404(Book, custom_id=book_id)
    return render(request, 'quillcart//view_book.html', {'book': book})

def update_book(request, book_id):
    book = get_object_or_404(Book, custom_id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('quillcart:book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'quillcart//update_book.html', {'form': form, 'book': book})

def delete_book(request, book_id):
    book = get_object_or_404(Book, custom_id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('quillcart:book_list')
    return render(request, 'quillcart//delete_book.html', {'book': book})


