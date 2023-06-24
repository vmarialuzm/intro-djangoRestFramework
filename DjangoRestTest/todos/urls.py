from rest_framework import routers
from .api import TodoViewSet,TestTodoViewSet,TestValidationViewSet

router = routers.DefaultRouter()

router.register('api/todos',TodoViewSet,'todos')
router.register('api/test/todos',TestTodoViewSet,'test_todos')
router.register('api/validation',TestValidationViewSet,'test_validation')

urlpatterns = router.urls