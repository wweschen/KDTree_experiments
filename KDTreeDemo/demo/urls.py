
from rest_framework import routers
from .api import DemoViewSet

router = routers.DefaultRouter()
router.register('api/demo',DemoViewSet,'')

urlpatterns = router.urls

