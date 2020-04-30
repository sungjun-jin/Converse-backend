from django.urls import path
from .views      import MainPageView, StoreView

urlpatterns = [
   path('', MainPageView.as_view()),
   path('stores', StoreView.as_view())
]
