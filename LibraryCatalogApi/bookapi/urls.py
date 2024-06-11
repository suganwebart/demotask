from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from bookapi import views


# API endpoints
urlpatterns = [
      # Your API URLs
      path('authors/', views.AuthorList.as_view(),name='author-list'),
      path('authors/<int:pk>/', views.AuthorDetail.as_view(), name='author-detail'),
      path('books/', views.BookList.as_view(),name='book-list'),
      path('books/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
      path('login/', views.LoginView.as_view(), name='login'),
      path('signup/', views.SignUpView.as_view(), name='signup'),
      path('logout/', views.DeleteTokenView.as_view(), name='delete-token'),
      path('users/', views.UserList.as_view(),name='customuser-list'),
      path('users/<int:pk>/', views.UserDetail.as_view(), name='customuser-detail'),
      
      

]

urlpatterns = format_suffix_patterns(urlpatterns)