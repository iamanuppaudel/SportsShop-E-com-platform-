from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name="index"),
    path ('browse/', views.browse, name="browse"),
    path('product/<str:pk>/', views.productdetails, name="productdetails"),
    path('categories/<str:slug>', views.categories, name="categories"),
    path('contact/', views.contact, name="contact"),
    path('blog/', views.blogpage, name="blogpage"),
    path('blog/<str:pk>/', views.blogdetail, name="blogdetail"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update-item/', views.updateItem, name="updateitem"),
    path('process_order/', views.processOrder, name="processorder"),
]
