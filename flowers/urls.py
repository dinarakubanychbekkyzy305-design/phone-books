from rest_framework.routers import DefaultRouter
from .views import FlowerViewSet

router = DefaultRouter()
router.register(r'flowers', FlowerViewSet)

urlpatterns = router.urls
