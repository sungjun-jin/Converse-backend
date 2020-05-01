from django.urls import path

from .views import FilterView, ProductView, DetailView

urlpatterns = [

    path('/filter/<str:category_name>', FilterView.as_view()),
    path('/category/<str:category_name>', ProductView.as_view()),
    path('/<str:product_code>', DetailView.as_view()),

]
