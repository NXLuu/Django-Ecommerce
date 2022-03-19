
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_product, name='manager'),
    path('emp', views.emp),  
    path(r'^add-product/$', views.add_product, name='add-product'),
    path('edit/<int:id>', views.edit),  
     path('update/<int:id>', views.update),  
      path('delete/<int:id>', views.destroy),  
    # path('product/<product_id>', views.product_details, name='product-details'),
    # path('wishlist/', views.wishlist, name='wishlist'),
]
