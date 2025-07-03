from django.urls import path
from users.views import LoginView, test

urlpatterns = [
    path('', LoginView.as_view(), name="login"),
]
