
from django.contrib import admin
from django.urls import path, include
from library_app.views import api
from django.contrib.auth import views as auth_views
from library_app import views
from library_app.views import custom_login_view

urlpatterns = [
    path('admin/', admin.site.urls),
     path('login/', custom_login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('api/', api.urls),
    path('', include('library_app.urls')),
]