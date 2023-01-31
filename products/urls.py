from django.urls import path

from .views import ProductList, ProductDetail, CommentCreateView

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('comment/<int:pk>/', CommentCreateView.as_view(), name='comment_create'),
    ]
