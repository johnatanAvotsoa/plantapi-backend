from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/scans/', include('scans.urls')),# <- ici ny historique
    path('api/accounts/', include('scans.urls')) , # <- ici les comptes utilisateurs
]
