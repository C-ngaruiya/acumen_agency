from django.urls import path
from . import views as my_views

urlpatterns = [
    path('', my_views.tenants, name='tenant-list-url'),
    path('<int:pk>', my_views.detail, name='tenant-detail-url'),
    path('create/', my_views.add_tenant, name='tenant-create-url'),
    path('update/<int:pk>', my_views.update_tenant, name='tenant-update-url'),
    path('delete/<int:pk>', my_views.delete, name='tenant-delete-url'),
]
