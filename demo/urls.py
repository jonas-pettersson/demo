from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('demo/', include('contacts.urls')),
    path('', RedirectView.as_view(url='demo/', permanent=True)),
    path('admin/', admin.site.urls),
]
