from django.contrib import admin
from bookapi.models import *
from django.utils.html import format_html

admin.site.site_header = 'Administration for Library Catalog RESTful API'
admin.site.site_title = 'Library Catalog API'
admin.site.index_title = 'Library Catalog API'

      
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
      model = CustomUser
      list_display = ['first_name', 'last_name', 'email', 'username', 'role', 'image_tag' ]
      
      def CustomUser_role(self, obj):
            return obj.user.role if obj.user else None
      CustomUser_role.short_description = 'User Role' 
      
      def image_tag(self, obj):
            return format_html('<img src="{}" width="50" />', obj.userimages.url) if obj.userimages else ''
      image_tag.short_description = 'Image' 
      
      
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
      model = Genre
      
      
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
      model = Author
      
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
      model = Book
      list_display = ['title', 'image_tag', 'language', 'price', 'author', 'publication_date' , 'user','user_role' , 'published', 'availability_status']
      list_filter = (
            'published',
            'publication_date',
            'availability_status',
      )
      def image_tag(self, obj):
            return format_html('<img src="{}" width="50" />', obj.bookimage.url) if obj.bookimage else ''
      image_tag.short_description = 'Image' 
      
      def user_role(self, obj):
            return obj.user.role if obj.user else None
      user_role.short_description = 'User Role'  
      
@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
      model = Publisher

