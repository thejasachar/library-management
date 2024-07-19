from django.http import JsonResponse
from ninja import NinjaAPI, Schema
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Book, Borrow
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/books')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_superuser:
                return redirect('/admin/')
            else:
                return redirect('/')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('home') 

api = NinjaAPI()

class BookSchema(Schema):
    title: str
    author: str
    isbn: str

class BorrowSchema(Schema):
    user_id: int
    book_id: int

# User Actions
@api.get("/books")
def book_list(request):
    books = Book.objects.all()
    user_id = request.user.id if request.user.is_authenticated else None
    return render(request, 'book_list.html', {'books': books, 'user_id': user_id})

@api.post("/borrow")
def borrow_book(request, payload: BorrowSchema):
    user = get_object_or_404(User, id=payload.user_id)
    book = get_object_or_404(Book, id=payload.book_id)

    if not book.available:
        raise HttpError(400, "This book is already borrowed.")

    borrow_record = Borrow(user=user, book=book)
    borrow_record.save()
    book.available = False
    book.save()
    return {"success": True, "message": "Book borrowed successfully!"}

@api.post("/return")
def return_book(request, payload: BorrowSchema):
    user = get_object_or_404(User, id=payload.user_id)
    book = get_object_or_404(Book, id=payload.book_id)
    
    borrow_record = get_object_or_404(Borrow, user=user, book=book, returned_at__isnull=True)
    borrow_record.returned_at = timezone.now()
    borrow_record.calculate_fine()  # Ensure fine is calculated
    borrow_record.save()
    
    book.available = True
    book.save()
    return {"success": True, "message": "Book returned successfully!", "fine_amount": borrow_record.fine_amount}

def borrow_book_view(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        book_id = request.POST.get('book_id')
        payload = BorrowSchema(user_id=user_id, book_id=book_id)
        result = borrow_book(request, payload)
        return JsonResponse(result)
    return render(request, 'borrow_book.html')

def return_book_view(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        book_id = request.POST.get('book_id')
        payload = BorrowSchema(user_id=user_id, book_id=book_id)
        result = return_book(request, payload)
        return JsonResponse(result)
    return render(request, 'return_book.html')

def admin_books(request):
    return render(request, 'admin_books.html')

def home(request):
    return render(request, 'home.html')

@api.exception_handler(Exception)
def custom_exception_handler(request, exc):
    return api.create_response(request, {"message": str(exc)}, status=400)
