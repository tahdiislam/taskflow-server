from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter()

router.register('list', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('update-status/<int:pk>/', views.TaskUpdateViewSet.as_view()),
]