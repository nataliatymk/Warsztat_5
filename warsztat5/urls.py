from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from photoalbum.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',MainView.as_view(), name="main_view"),
    path('login/',LoginView.as_view(), name="login_view"),
    path('logout/',LogoutView.as_view(), name="logout_view"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
