from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('detail/<int:pk>', views.ContactDetailView.as_view(), name='contact_detail'),
]
