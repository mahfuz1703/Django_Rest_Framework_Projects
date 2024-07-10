from django.urls import path
from .views import *
urlpatterns = [
    # path('booklist', views.books, name="books"),
    path('booklist', BookList.as_view(), name="booklist"),
    path('booklist/<int:pk>', Book.as_view(), name="booklist"),

    # path('menu_items', views.MenuItemView.as_view(), name="menu_item"),
    path('menu_items/', menu_items, name="menu_items"),
    path('menu_items/<int:pk>', SingleMenuItemView.as_view(), name="menu_item"),

    path('categories', CategoriesView.as_view()),
    path('menu-items', MenuItemsView.as_view()),
]