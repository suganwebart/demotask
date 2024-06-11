from rest_framework import serializers
from bookapi.models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class BookSerializer(serializers.ModelSerializer):

      class Meta:
            model = Book
            fields = ['url', 'id', 'title', 'language', 'description', 'price',
                        'genres', 'author', 'publisher', 'user', 'publication_date', 'published', 'availability_status', 'bookimage']
            
class AuthorSerializer(serializers.ModelSerializer):

      class Meta:
            model = Author
            fields = ['url', 'name', 'bio']
            

class SignupSerializer(serializers.ModelSerializer):
      password = serializers.CharField(write_only=True)
      
      class Meta:
            model = CustomUser
            fields = ['id', 'username','email', 'password','first_name', 'last_name']
            #
            # extra_kwargs = {'password': {'write_only': True}}


      def create(self, validated_data):
            instance = CustomUser.objects.create_user(**validated_data)
            Token.objects.create(user=instance)
            return instance

      
      def to_representation(self, instance):
            # Customize the JSON representation of the instance
            representation = super().to_representation(instance)
            token = instance.auth_token.key   
            representation['success'] = 'User created successfully. Your token is generated'
            representation['token'] = token

            return representation

class LoginSerializer(serializers.Serializer):
      
      username = serializers.CharField()
      password = serializers.CharField(write_only=True)

      def validate(self, data):
            username = data.get('username')
            password = data.get('password')

            # Your custom authentication logic
            user = authenticate(username=username, password=password)
            if not user:
                  raise serializers.ValidationError("Incorrect username or password")

            data['user'] = user
            return data
      
      
