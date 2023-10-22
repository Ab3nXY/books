import json
from .forms import BookForm
from .models import Book 
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Sum


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


def book_dashboard(request):
    # Fetch book data from the database
    book_data = Book.objects.all()

    # Calculate the total number of books
    total_books = Book.objects.count()

    # Calculate the total distribution expense
    total_expense = Book.objects.aggregate(Sum('distribution_expense'))['distribution_expense__sum'] or 0

    # Group books by category and count the number of books in each category
    category_counts = Book.objects.values('category').annotate(count=Count('category'))

    # Prepare data for the bar chart
    category_data = {
        'labels': [category_count['category'] for category_count in category_counts],
        'datasets': [
            {
                'label': 'Number of Books',
                'data': [category_count['count'] for category_count in category_counts],
                'backgroundColor': 'rgba(54, 162, 235, 0.6',  # You can choose your own color
            }
        ]
    }

    # Prepare data for the total expense pie chart
    expense_data = {
        'labels': ['distribution_expense', 'Other'],
        'datasets': [
            {
                'data': [total_expense, 0],  # Total expense and other expenses (0 in this case)
                'backgroundColor': ['rgba(255, 99, 132, 0.6)', 'rgba(54, 162, 235, 0.6'],  # You can choose your own colors
            }
        ]
    }

    context = {
        'book_data': book_data,
        'category_counts': category_counts,
        'total_books': total_books,
        'total_expense': total_expense,
        'category_data': category_data,
        'expense_data': expense_data,
    }
    return render(request, 'quillcart//dashboard.html', context)

