from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailOnlyModelBackend(ModelBackend):
    """
    Authenticate strictly by email+password.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Djoser will pass your email in the `username` argument.
        User = get_user_model()
        if username is None or password is None:
            return None
        try:
            user = User.objects.get(email__iexact=username)
        except User.DoesNotExist:
            return None
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None

    def get_user(self, user_id):
        return get_user_model().objects.filter(pk=user_id).first()
