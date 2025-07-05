from django.urls import path
# from users.views import LoginView
from .views import acceuil

urlpatterns = [
    # path('', LoginView.as_view(), name="login"),
    path('',acceuil, name='acceuil')
]
