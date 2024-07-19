# Library Management System

This is a Library Management System built with Django. It allows users to manage book borrowing and returning, and provides an admin interface for managing the library's collection of books.

## Features

- User authentication and registration
- Borrow and return books
- Admin interface for managing books and borrow records
- API endpoints for book and borrow operations
- Responsive web interface

## Project Structure

```bash
library_project/
├── library_app/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── signals.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── book_list.html
│   │   ├── borrow_book.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── return_book.html
│   │   ├── signup.html
│   ├── urls.py
│   ├── views.py
│   ├── static/
│   │   ├── styles.css
│   │   ├── scripts.js
├── library_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── db.sqlite3
├── manage.py
```
## Installation
```bash
Prerequisites
Python 3.8+
Django 5.0.6
Virtualenv (recommended)
```
# Steps
## Clone the repository:
```bash
git clone https://github.com/yourusername/library_project.git
cd library_project
```
## Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
## Apply migrations:
```bash
python manage.py migrate
```
## Create a superuser for accessing the admin interface:
```bash
python manage.py createsuperuser
```
## Run the development server:
```bash
python manage.py runserver
```
## Open your browser and go to http://127.0.0.1:8000/ to see the application.

# Usage
## User Interface
Home Page: Displays the homepage of the library system.
Login: User login page.
Sign Up: User registration page.
Book List: Displays a list of books available in the library.
Borrow Book: Allows authenticated users to borrow a book.
Return Book: Allows authenticated users to return a borrowed book.
Admin Books: Admin interface to manage books.
## Admin Interface
The admin interface is accessible at http://127.0.0.1:8000/admin/. Use the superuser credentials created during installation to log in.

## API Endpoints
GET /api/books/: List all books.
POST /api/borrow/: Borrow a book.
POST /api/return/: Return a book.

# Project Files
## settings.py
Contains the Django settings for the project, including configuration for the database, installed apps, middleware, templates, and static files.

## urls.py
Defines the URL routes for the project, including the paths for the admin interface, login, logout, signup, and the API endpoints.

## models.py
Defines the data models for the application, including Book, Borrow, and UserProfile.

## views.py
Contains the view functions that handle requests and return responses for the various pages and API endpoints.

## admin.py
Configures the admin interface for managing the Book, Borrow, and UserProfile models.

## signals.py
Contains signal handlers that automatically create and save UserProfile instances when User instances are created or saved.

## static/styles.css
Contains the CSS styles for the application's frontend.

## static/scripts.js
Contains the JavaScript code for the application's frontend.

## templates/
Contains the HTML templates for the various pages in the application, including base.html, book_list.html, borrow_book.html, home.html, login.html, return_book.html, and signup.html.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements
Django Ninja for the API framework.

## Contact
For any inquiries or feedback, please contact [thejas0123@gmail.com].


