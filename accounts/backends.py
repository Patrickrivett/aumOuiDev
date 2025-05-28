# accounts/backends.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailOrUsernameModelBackend(ModelBackend):
    """
    Allow authentication with either `username` or `email`.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        # If Djoser passes in a different field, grab it:
        username = username or kwargs.get(User.USERNAME_FIELD)
        if username is None or password is None:
            return None

        # Try email first if it looks like one:
        lookup = {'email': username} if '@' in username else {'username': username}
        try:
            user = User.objects.get(**lookup)
        except User.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
