
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from myapp.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'viewses', ApiViewSets)


urlpatterns = [
    path("", HelloView.as_view(), name='hello'),
    path("viewsets/", include(router.urls)),
    # path("modelviews/", ApiViewSets.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update',
    #                                         'delete': 'destroy'}), name='model_views'),
    # path("userinfo/<int:pk>", UserDetail.as_view())

]

