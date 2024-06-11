from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import permissions

from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

from bookapi.models import *
from bookapi.serializers import *

import pdb


# Create your views here.
class BookList(generics.ListCreateAPIView):
      """"
      List all Books, or create a new Books. 
      """
      authentication_classes = [TokenAuthentication]
      permission_classes = [permissions.IsAuthenticated]

      queryset = Book.objects.all()
      serializer_class = BookSerializer
      
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
      
      """
      Retrieve, update or delete a Book instance.
      """
      authentication_classes = [TokenAuthentication]
      permission_classes = [permissions.IsAuthenticated]
      
      queryset = Book.objects.all()
      serializer_class = BookSerializer

class AuthorList(generics.ListCreateAPIView):
      """"
      List all Authors, or create a new Authors. 
      """
      authentication_classes = [TokenAuthentication]
      permission_classes = [permissions.IsAuthenticated]
      
      queryset = Author.objects.all()
      serializer_class = AuthorSerializer
      
class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
      
      """
      Retrieve, update or delete a Author instance.
      """

      authentication_classes = [TokenAuthentication]
      permission_classes = [permissions.IsAuthenticated]
      
      queryset = Author.objects.all()
      serializer_class = AuthorSerializer
      

class SignUpView(generics.CreateAPIView):
      
      """
      Signup to get token
      """
      
      permission_classes = (permissions.AllowAny,)
      serializer_class = SignupSerializer

      def post(self, request, *args, **kwargs):
            return self.create(request, *args, **kwargs)
      

class LoginView(generics.GenericAPIView):
      
      """
      Login to get token
      """
      permission_classes = (permissions.AllowAny,)
      serializer_class = LoginSerializer

      def post(self, request, *args, **kwargs):
            
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            response_data = serializer.data
            token, created = Token.objects.get_or_create(user=user)
            response_data['token'] = token.key

            return Response(response_data)
            
class DeleteTokenView(generics.GenericAPIView):
      
      """
      Delete token
      """
      authentication_classes = [TokenAuthentication]
      permission_classes = [permissions.IsAuthenticated]
            
      def post(self, request, *args, **kwargs):
            # Get the authenticated user
            user = request.user
            # Get the user's token
            try:
                  token = Token.objects.get(user=user)
                  # Delete the token
                  token.delete()
                  return Response({"detail": "Token deleted successfully.", "username": user.username})
            except Token.DoesNotExist:
                  return Response({"detail": "Token not found."}, status=status.HTTP_404_NOT_FOUND)