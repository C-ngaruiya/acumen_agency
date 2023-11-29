from django.urls import path
from . import views as my_views

urlpatterns = [
    path('', my_views.properties, name='property-list-url'),
    path('<int:pk>', my_views.detail, name='property-detail-url'),
    path('create/', my_views.add_property, name='property-create-url'),
    path('update/<int:pk>', my_views.update_property, name='property-update-url'),
    path('delete/<int:pk>', my_views.delete, name='property-delete-url'),
    path('pay/<int:pk>', my_views.pay, name='property-pay-url')
]
