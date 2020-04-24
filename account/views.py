import json,bcrypt,jwt

from django.views import View
from django.http            import HttpResponse,JsonResponse
from django.core.exceptions import ValidationError

from .models                import User,Gender
from converse.settings      import SECRET_KEY

class SignUpView(View):
    def post(self,request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(email = data['email']).exists():
                return JsonResponse({'Message' : 'USER_ALREADY_EXISTS'}, status = 400)
            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'),bcrypt.gensalt())
            User (
                email = data['email'],
                password = hashed_password.decode('utf-8'),
                name = data['name'],
                phone = data['phone'],
                birth = data['birth'],
                gender = Gender.objects.get(name = data['gender']),
                email_confirm = data['email_confirm'],
                text_confirm = data['text_confirm']
            ).save()
            return HttpResponse(status=200)
        except KeyError:
            return JsonResponse({'Message':'INVALID_KEY'},status=400)
        except ValidationError:
            return JsonResponse({'Message': 'VALIDATION_ERROR'}, status=400)
        except AttributeError:
            return JsonResponse({'Message': 'ATTRIBUTE_ERROR'},status=400)

class SignInView(View):
    def post(self,request):
        data = json.loads(request.body)
        try:
            data_email = data['email']
            data_password = data['password']
            if User.objects.filter(email = data_email).exists():
                user = User.objects.get(email = data_email)
                if bcrypt.checkpw(data_password.encode('utf-8'),user.password.encode('utf-8')):
                    access_token = jwt.encode({'user_id':user.id},SECRET_KEY,algorithm = 'HS256')
                    return JsonResponse({'access_token':access_token.decode('utf-8')}, status=200)
            return JsonResponse({'Message':'INVALID_USER'}, status = 401)
        except  KeyError:
            return JsonResponse({'Message':'INVALID_KEY'}, status=400)
        except ValidationError:
            return JsonResponse({'Message': 'VALIDATION_ERROR'}, status=400)
        except AttributeError:
            return JsonResponse({'Message': 'ATTRIBUTE_ERROR'},status=400)

