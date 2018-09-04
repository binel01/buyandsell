from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .models import Product, Category, UserProfile

# Product views
class ProductDetailView(DetailView):
    model = Product
    template_name = "core/product_detail.html"

class ProductListView(ListView):
    model = Product
    template_name = "core/product_list.html"

class ProductCreateView(CreateView):
    model = Product
    template_name = "core/product_create.html"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ProductUpdateView(UpdateView):
    model = Product
    template_name = "core/product_update.html"

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "core/product_delete.html"

# Product Categories views
class CategoryDetailView(DetailView):
    model = Category
    template_name = "core/category_detail.html"

class CategoryListView(ListView):
    model = Category
    template_name = "core/category_list.html"

class CategoryCreateView(CreateView):
    model = Category
    template_name = "core/category_create.html"

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = "core/category_update.html"

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "core/category_delete.html"

# UserProfile views
class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = "core/userprofile_detail.html"

class UserProfileListView(ListView):
    model = UserProfile
    template_name = "core/userprofile_list.html"

class UserProfileCreateView(CreateView):
    model = UserProfile
    template_name = "core/userprofile_create.html"

class UserProfileUpdateView(UpdateView):
    model = UserProfile
    template_name = "core/userprofile_update.html"

class UserProfileDeleteView(DeleteView):
    model = UserProfile
    template_name = "core/userprofile_delete.html"
