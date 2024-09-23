from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()

router.register('list', views.CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.RegistrationViewSet.as_view()),
    path('confirm/<uid64>/<token>/', views.activate),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view())
]