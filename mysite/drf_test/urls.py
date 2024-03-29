# drf_test/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

"""
The REST Framework router will make sure our requests end up at the right resource dynamically.
If we add or delete items from the database, the URLs will update to match. Cool right?
"""


router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
