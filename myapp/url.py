from django.urls import path
from .views import signup, signup_admin, login, create_train, train_availability

urlpatterns = [
    path('api/signup/', signup),
    path('api/signup/admin', signup_admin),
    path('api/login/', login),
    path('api/trains/create/', create_train),
    path('api/trains/availability/', train_availability)
]
