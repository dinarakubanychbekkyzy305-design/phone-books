from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookVeiwSet


router = DefaultRouter()
router.register(r'books', BookVeiwSet)

urlpatterns = [
    path('', include(router.urls))
]