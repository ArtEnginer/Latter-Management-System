from django.contrib import admin
from django.urls import path, include
from surat_menyurat import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.login_redirect, name='login_redirect'),
    path('home/', views.home, name='home'),    
    path('surat/', include('surat_menyurat.urls', namespace="surat")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
