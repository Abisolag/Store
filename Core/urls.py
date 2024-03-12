from django.urls import path
from . import views
urlpatterns =[
    path('', views.index, name='index'),
    path('store/', views.store, name='store'),
    # path('product', views.product, name='product'),
    path('checkout/', views.checkout, name='checkout'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('upload/', views.upload_product, name='upload'),
    path('product_detail/<int:pk>', views.ProductDetailView.as_view(),name='product_detail'),
    path('add-cart/<int:product_id>', views.add_to_cart, name='add-cart'),
    path('subtract-cart/<int:product_id>', views.subtract_from_cart, name='subtract'),
    path('remove-cart/<int:item_id>', views.remove_from_cart, name='remove-cart'),
    path('increase_cart/<int:pk>', views.increase_cart_quantity, name='increase_cart'),
    
]
