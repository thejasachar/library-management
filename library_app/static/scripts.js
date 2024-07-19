$(document).ready(function() {
    // Fetch books for the book list
    if ($('#book-list').length) {
        $.get('/books/', function(data) {
            data.forEach(function(book) {
                $('#book-list').append('<li>' + book.title + ' by ' + book.author + '</li>');
            });
        }).fail(function(xhr) {
            alert('Failed to fetch books: ' + xhr.responseText);
        });
    }

    // Borrow a book
    $('#borrow-form').submit(function(e) {
        e.preventDefault();
        $.post($(this).attr('action'), $(this).serialize())
            .done(function(data) {
                alert(data.message);
            })
            .fail(function(xhr) {
                const response = JSON.parse(xhr.responseText);
                alert('Failed to borrow book: ' + response.message);
            });
    });

    // Return a book
    $('#return-form').submit(function(e) {
        e.preventDefault();
        $.post($(this).attr('action'), $(this).serialize())
            .done(function(data) {
                alert(data.message);
                if (data.fine_amount > 0) {
                    $('#fine-message').text('Fine Amount: $' + data.fine_amount);
                } else {
                    $('#fine-message').text('');
                }
            })
            .fail(function(xhr) {
                const response = JSON.parse(xhr.responseText);
                alert('Failed to return book: ' + response.message);
            });
    });

    // Admin - Fetch and manage books
    if ($('#admin-book-list').length) {
        $.get('/admin/books/', function(data) {
            data.forEach(function(book) {
                $('#admin-book-list').append('<li>' + book.title + ' by ' + book.author + '</li>');
            });
        }).fail(function(xhr) {
            alert('Failed to fetch admin books: ' + xhr.responseText);
        });

        $('#add-book-form').submit(function(e) {
            e.preventDefault();
            $.post('/admin/books/', {
                title: $('#title').val(),
                author: $('#author').val(),
                isbn: $('#isbn').val()
            })
            .done(function(data) {
                alert('Book added successfully!');
                location.reload();
            })
            .fail(function(xhr) {
                const response = JSON.parse(xhr.responseText);
                alert('Failed to add book: ' + response.message);
            });
        });
    }
});
