
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from myapp.views import *


urlpatterns = [
    path("", HelloView.as_view(), name='hello'),
    path("modelviews/", ApiViewSets.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update',
                                            'delete': 'destroy'}), name='model_views'),
    path("userinfo/<int:pk>", UserDetail.as_view())

]
urlpatterns = format_suffix_patterns(urlpatterns)
