from rest_framework.authentication import BaseAuthentication
import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
import base64

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        user = None
        token = None
        
        try:
            token = request.COOKIES['token']
            print(token.strip('b').strip("'"))
            data = jwt.decode(token.strip('b').strip("'"), settings.SECRET_KEY, algorithms=['HS256'])
            user = get_user_model().objects.get(username=data['email'])
        except:
            return None
            
        return (user, token)