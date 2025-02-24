from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, ConfirmUserSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    """Регистрация пользователя."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {'message': 'Пользователь зарегистрирован. Проверьте код подтверждения.'},
            status=status.HTTP_201_CREATED
        )

class ConfirmUserView(generics.GenericAPIView):
    """Подтверждение пользователя по коду."""
    serializer_class = ConfirmUserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
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

