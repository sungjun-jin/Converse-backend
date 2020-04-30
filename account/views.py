import json
import bcrypt
import jwt
import re

from django.views           import View
from django.http            import HttpResponse,JsonResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from .models                import User
from converse.settings      import SECRET_KEY

class SignUpView(View):
    VALIDATIONS = {
        'password' : lambda password : True if re.match(r'(?=.*[A-Za-z])(?=.*[!@#$%^&*()_+=-])(?=.*[0-9]){8,}', password) else False,
        'birth'    : lambda birth    : True if re.match(r'(?=.*[0-9]{8,})', birth) else False,
        'phone'    : lambda phone    : True if '-' not in phone else False
    }

    def post(self,request):
        data = json.loads(request.body)
        try:
            validate_email(data['email'])

            if User.objects.filter(email = data['email']).exists():
                return JsonResponse({'Message' : 'USER_ALREADY_EXISTS'}, status = 400)

            for validation_name, validate in self.VALIDATIONS.items():
                if not validate(data[validation_name]):
                    return JsonResponse({'Message' : f'{validation_name.upper()}_VALIDATION_ERROR'}, status = 400)

            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
            User (
                email         = data['email'],
                password      = hashed_password.decode('utf-8'),
                name          = data['name'],
                gender        = data['gender'],
                phone         = data['phone'],
                birth         = data['birth'],
                email_confirm = data['email_confirm'],
                text_confirm  = data['text_confirm']
            ).save()

            return JsonResponse({'Message' : 'OK'}, status = 200)

        except KeyError:
            return JsonResponse({'Message':'INVALID_KEY'}, status = 400)

        except ValidationError:
            return JsonResponse({'Message': 'VALIDATION_ERROR'}, status = 400)

class SignInView(View):
    def post(self,request):
        data = json.loads(request.body)
        try:

            if User.objects.filter(email = data['email']).exists():
                user = User.objects.get(email = data['email'])

                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                    access_token = jwt.encode({'user_id' : user.id}, SECRET_KEY, algorithm = 'HS256')
                    return JsonResponse({'access_token' : access_token.decode('utf-8')}, status = 200)

            return JsonResponse({'Message' : 'INVALID_USER'}, status = 401)

        except KeyError:
            return JsonResponse({'Message' : 'INVALID_KEY'}, status = 400)
