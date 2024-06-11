from rest_framework import permissions
import pdb

class IsLibrarianOrReadOnly(permissions.BasePermission):
      """
      Custom permission to only allow librarians to perform write operations.
      """

      def has_permission(self, request, view):
            
            
            # Read permissions are allowed to any request, so we'll always allow GET, HEAD, or OPTIONS requests.
            if request.method in permissions.SAFE_METHODS:
                  return True

            # Write permissions are only allowed to users with the librarian role.
            if request.user.is_authenticated:
            # Check if the user has the 'Librarian' role
                  return request.user.role == 'librarian'
            else:
            # If the user is not authenticated, deny permission
                  return False
            