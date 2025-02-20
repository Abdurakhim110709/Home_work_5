from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Создаёт пользователя, делает его неактивным и генерирует confirmation_code."""
        user = User.objects.create_user(**validated_data)
        user.is_active = False
        user.generate_confirmation_code()
        return user

class ConfirmUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField(max_length=6)
