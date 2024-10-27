from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import Author

class AuthorBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            # Find the author by email
            author = Author.objects.get(email=email)
            # Check if the password is correct
            if author and check_password(password, author.password):
                return author
        except Author.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Author.objects.get(pk=user_id)
        except Author.DoesNotExist:
            return None
