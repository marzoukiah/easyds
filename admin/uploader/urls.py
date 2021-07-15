from rest_framework.routers import SimpleRouter
from .views import DropBoxViewSet

router = SimpleRouter()
router.register('accounts', DropBoxViewSet)
urlpatterns = router.urls