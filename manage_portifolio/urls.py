from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('institucional.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('account/', include('account.urls')),
    path('account/', include('django.contrib.auth.urls')),
]
