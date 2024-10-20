from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from accounts.serializers import UserSerializer
from .models import User
from jwt import PyJWT,encode,decode,ExpiredSignatureError
import datetime
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        phone=request.data['phone']
        password=request.data['password']
        user=User.objects.filter(phone=phone).first()
        if user is None:
            raise AuthenticationFailed('User not found')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        # payload={
        #     'id': user.id,
        #     'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        #     'iat': datetime.datetime.utcnow()
        # }
        # token=encode(payload,'secret', algorithm='HS256').decode('utf-8')
        token = encode({
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)},
            'secret', algorithm='HS256')
        response = Response()
        response.data={
            'jwt':str(token)
        }
        response.set_cookie(key='jwt', value=str(token), httponly=True)
        return response
        # return Response({
        #     'jwt':str(token)
        #
        # })
# class UserView(APIView):
#     def get(self, request):
#         token=request.COOKIES.get('jwt')
#         if not token:
#             raise AuthenticationFailed('User not found')
#         try:
#             payload=decode(token,'secret', ['HS256'])
#         except ExpiredSignatureError:
#             raise AuthenticationFailed('User not found')
#         user=User.objects.filter(id=payload['id']).first()
#         serializer = UserSerializer(user)
#         response=Response(serializer.data)
