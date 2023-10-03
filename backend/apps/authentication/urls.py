from django.urls import path, include

from apps.authentication import api

paths = [
    path('register/', api.RegisterView.as_view(), name='register'),
    path('login/', api.LoginView.as_view(), name='login'),
    path('logout/', api.LogoutView.as_view(), name='logout'),
]

urlpatterns = [
    path('authentication/', include(paths))
]
