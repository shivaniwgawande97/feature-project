from django.contrib import admin
from django.urls import path
from product import views
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("product/", views.ProductList.as_view()),
    path("generic/product/<int:id>/",views.GenericAPIView.as_view())

]