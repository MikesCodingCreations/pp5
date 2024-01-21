from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name="products"),
    path('<int:product_id>/', views.product_detail, name="product_detail"),
    path('add/', views.add_a_product, name="add_a_product"),
    path('edit/<int:product_id>/', views.edit_a_product, name="edit_a_product"),
    path('delete/<int:product_id>/', views.delete_a_product, name="delete_a_product"),
]
