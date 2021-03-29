from rest_framework import routers
from .api import TodoVeiwSet

router = routers.DefaultRouter()
router.register('api/todo', TodoVeiwSet, 'todo')

urlpatterns = router.urls
