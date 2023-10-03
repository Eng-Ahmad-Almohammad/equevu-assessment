"""Modula that provide custom DRF permissions classes."""

from rest_framework import permissions


class IsAdminUserOrPostOnly(permissions.BasePermission):
    """Custom permission class to control access based on user type and HTTP method."""

    message = "You do not have permission to access this resource."

    def has_permission(self, request, view):
        """Check if the user has permission to access the view.

        Args:
            request (HttpRequest): The HTTP request object.
            view (View): The view handling the request.

        Returns:
            bool: True if the request is allowed, False otherwise.
        """
        if request.method == "GET" and not request.is_admin:
            return False  # Admin user, allow access
        return True
