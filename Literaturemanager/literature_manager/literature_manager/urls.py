"""
URL configuration for literature_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from literature_system.views import(
    home_screen_view,
    book_data_screen_view,
    user_register,
    add_book,
    login_view,
    logout_view,
    profile_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name="home"),
    path('BookData/', book_data_screen_view, name="book_data"),
    path('Registration/', user_register, name="user_registry"),
    path('BookAdd/', add_book, name='add_book'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

