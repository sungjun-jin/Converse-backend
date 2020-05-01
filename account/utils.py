import jwt

from django.http            import JsonResponse

from converse.settings      import SECRET_KEY
from .models                import User

def login_required(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = jwt.decode(request.headers['Authorization'], SECRET_KEY, algorithm = 'HS256')
            request.user = User.objects.get(id = access_token['user_id'])
            return func(self, request, *args, **kwargs)

        except jwt.DecodeError:
            return JsonResponse({'Message' : 'INVALID_TOKEN'}, status = 400)

    return wrapper
