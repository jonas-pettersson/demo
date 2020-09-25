from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'contacts', views.ContactViewSet)
router.register(r'companies', views.CompanyViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('api/', include(router.urls)),
    # path('api/contacts/', views.ContactViewSet.as_view({'get': 'queryset'})),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('detail/<int:pk>', views.ContactDetailView.as_view(), name='contact_detail'),
    path('detail/<int:pk>/update/',
         views.ContactUpdateView.as_view(), name='contact_update'),
]
