from django.urls import path, include

urlpatterns = [
    path('account', include('account.urls')),
    path('product', include('product.urls')),
    path('service', include('service.urls')),
    path('', include('foundation.urls')),
]
