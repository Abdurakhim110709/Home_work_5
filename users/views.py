from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, ConfirmUserSerializer

User = get_user_model()

class RegisterView(APIView):
    """Регистрация пользователя."""
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Пользователь зарегистрирован. Проверьте код подтверждения.'},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConfirmUserView(APIView):
    """Подтверждение пользователя по коду."""
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ConfirmUserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            code = serializer.validated_data['confirmation_code']

            try:
                user = User.objects.get(username=username, confirmation_code=code)
                user.is_active = True
                user.confirmation_code = None
                user.save()

                token, _ = Token.objects.get_or_create(user=user)
                return Response({'message': 'Аккаунт подтвержден!', 'token': token.key}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({'error': 'Неверное имя пользователя или код'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
