from django.urls import path
from .views import RegisterView, ConfirmUserView

urlpatterns = [
    path('register/',RegisterView.as_view(), name='register'),
    path('confirm/',ConfirmUserView.as_view(), name='confirm'),
]
