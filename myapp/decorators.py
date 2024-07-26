from rest_framework.response import Response
from rest_framework import status
import jwt
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from functools import wraps
import logging
from .models import User

def validate_apikey(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        apikey = request.headers.get('apikey')
        if apikey != '12345':
            return Response({'detail': 'Invalid API Key'}, status=status.HTTP_403_FORBIDDEN)
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func

# myapp/decorators.py

def jwt_authentication_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        logger = logging.getLogger('django')
        logger.info('asdsadsadasdsadsadsas')
        auth_header = request.headers.get('Authorization')
        
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
            try:
                logger.info('token',token)
                print('token', token)
                payload = jwt.decode(token, '12')
                user_id = payload.get('id')
                logger.info('user_id', user_id)
                try:
                    user = User.objects.get(id=user_id)
                    request.user = user
                except User.DoesNotExist:
                    return JsonResponse({'detail': 'User not found', 'code': user_id}, status=401)
            except jwt.ExpiredSignatureError:
                return JsonResponse({'detail': 'Token has expired', 'code': 'token_expired'}, status=401)
            except jwt.InvalidTokenError:
                return JsonResponse({'detail': 'Invalid token', 'code': 'invalid_token'}, status=401)
        else:
            return JsonResponse({'detail': 'Authentication credentials were not provided.'}, status=401)

        return view_func(request, *args, **kwargs)

    return _wrapped_view
