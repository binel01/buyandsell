from django.urls import path, include

from . import views

# Product Urls
urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('product/create/', views.ProductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),
]

# Category Urls
urlpatterns += [
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('category/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),
]

# UserProfile Urls
urlpatterns += [
    path('profiles/', views.UserProfileListView.as_view(), name='profile-list'),
    path('profile/<int:pk>/', views.UserProfileDetailView.as_view(), name='profile-detail'),
    path('profile/create/', views.UserProfileCreateView.as_view(), name='profile-create'),
    path('profile/<int:pk>/update/', views.UserProfileUpdateView.as_view(), name='profile-update'),
    path('profile/<int:pk>/delete/', views.UserProfileDeleteView.as_view(), name='profile-delete'),
]
