from rest_framework.routers import DefaultRouter

from template.views import EntityViewSet

v1_router = DefaultRouter()
v1_router.register(r'things', EntityViewSet)
