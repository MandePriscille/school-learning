from django.urls import path
# from users.views import LoginView
from .views import acceuil, user_login, user_register, user_logout

urlpatterns = [
    # path('', LoginView.as_view(), name="login"),
    path('',acceuil, name='acceuil'),
    path('enregistre/', user_register, name="register"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout")
]

