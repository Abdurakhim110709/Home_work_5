from django.contrib.auth.models import AbstractUser
from django.db import models
import random

class User(AbstractUser):
    # По умолчанию is_active=False – пользователь не может войти в систему до подтверждения
    is_active = models.BooleanField(default=False)
    confirmation_code = models.CharField(max_length=6, blank=True, null=True)

    def generate_confirmation_code(self):
        """Генерирует случайный 6-значный код подтверждения и сохраняет пользователя."""
        self.confirmation_code = str(random.randint(100000, 999999))
        self.save()
