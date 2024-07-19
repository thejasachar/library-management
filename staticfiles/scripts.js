// library_app/static/scripts.js

$(document).ready(function() {
    // Fetch books for the book list
    if ($('#book-list').length) {
        $.get('/api/books/', function(data) {
            data.forEach(function(book) {
                $('#book-list').append('<li>' + book.title + ' by ' + book.author + '</li>');
            });
        });
    }

    // Borrow a book
    $('#borrow-form').submit(function(e) {
        e.preventDefault();
        $.post('/api/borrow/', {
            user_id: $('#user-id').val(),
            book_id: $('#book-id').val()
        }, function(data) {
            alert('Book borrowed successfully!');
        }).fail(function() {
            alert('Failed to borrow book.');
        });
    });

    // Return a book
    $('#return-form').submit(function(e) {
        e.preventDefault();
        $.post('/api/return/', {
            user_id: $('#user-id').val(),
            book_id: $('#book-id').val()
        }, function(data) {
            alert('Book returned successfully!');
        }).fail(function() {
            alert('Failed to return book.');
        });
    });

    // Admin - Fetch and manage books
    if ($('#admin-book-list').length) {
        $.get('/api/admin/books/', function(data) {
            data.forEach(function(book) {
                $('#admin-book-list').append('<li>' + book.title + ' by ' + book.author + '</li>');
            });
        });

        $('#add-book-form').submit(function(e) {
            e.preventDefault();
            $.post('/api/admin/books', {
                title: $('#title').val(),
                author: $('#author').val(),
                isbn: $('#isbn').val()
            }, function(data) {
                alert('Book added successfully!');
                location.reload();
            }).fail(function() {
                alert('Failed to add book.');
            });
        });
    }
});
