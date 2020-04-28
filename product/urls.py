from django.urls import path

from .views import DetailView

urlpatterns = [

    path('/<str:product_code>', DetailView.as_view()),

]
