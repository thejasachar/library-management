from django.contrib import admin
from .models import Book, Borrow, UserProfile

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'isbn', 'available')
    list_filter = ('available',)
    search_fields = ('title', 'author', 'isbn')

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrowed_at', 'due_date', 'returned_at', 'fine_amount')
    list_filter = ('returned_at',)
    search_fields = ('user__username', 'book__title')

    def save_model(self, request, obj, form, change):
        if obj.returned_at:
            obj.calculate_fine()
        super().save_model(request, obj, form, change)

