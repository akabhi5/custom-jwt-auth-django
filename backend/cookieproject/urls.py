from django.contrib import admin
from django.urls import path
from cookieapp.views import LoginView, LogoutView, SecureView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('secure/', SecureView.as_view()),
]