
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_page, name='home_name'),


    path('', include('users.urls', namespace='users')),
    path('app1', include('app1.urls', namespace='app1')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
