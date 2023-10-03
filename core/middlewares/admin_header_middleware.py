"""Custom middleware.

Since we are not using a full authentication system so we will differ
between the admin and the other users by checking the X-ADMIN header value
and inject is_admin property in the request so it will be accessible over the
request lifecycle.
"""


class AdminHeaderMiddleware:
    """Custom middleware.

    This middleware will inject is_admin property in the request
    with a boolean value based on the X-ADMIN header value.
    """

    def __init__(self, get_response):
        """Initialize the AdminHeaderMiddleware object.

        Args:
            get_response: It has a reference for the next
            middleware or view if it the last middleware

        Returns:
            None: returns None
        """
        self.get_response = get_response

    def __call__(self, request):
        """Call this method to authenticate admin.

        Args:
            request (HttpRequest): HttpRequest object

        Returns:
            HttpResponse: An HttpResponse object
        """
        if request.headers.get("X-ADMIN") == "1":  # noqa: WPS502
            request.is_admin = True
        else:
            request.is_admin = False

        return self.get_response(request)
