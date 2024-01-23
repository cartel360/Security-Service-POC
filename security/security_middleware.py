from functools import wraps
from django.core.exceptions import PermissionDenied
from knox.models import AuthToken


def check_role(required_role):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            auth_header = request.headers.get('Authorization')
            if auth_header:
                token = auth_header.split(' ')[1]
                print(token)
                try:
                    user = decode_token(token)
                    # request.user = user
                except AuthToken.DoesNotExist:
                    raise PermissionDenied("Unauthorized: Invalid token.")
            else:
                raise PermissionDenied("Unauthorized: Token missing.")
            
            if user.is_authenticated:
                print("user is authenticated")
                user_groups = user.usergroupuser_set.all()
                print(user_groups)
                for user_group in user_groups:
                    roles = user_group.user_group.roles.all()
                    for role in roles:
                        if role.name == required_role:
                            return view_func(request, *args, **kwargs)
                raise PermissionDenied("Unauthorized: You do not have the required role.")
            
            raise PermissionDenied("Unauthorized: User is not authenticated.")
        return wrapper
    return decorator


def decode_token(token):
    try:
        # Get the fisrt 8 characters of the token
        user_token = token[:8]
        token_instance = AuthToken.objects.get(token_key=user_token)
        user = token_instance.user
        return user
    except AuthToken.DoesNotExist:
        return None