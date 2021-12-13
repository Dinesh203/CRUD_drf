
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from crudapp.views import *


urlpatterns = [
    # path("", UserDetail.as_view()),
    path("userinfo/<int:pk>", UserDetail.as_view()),
    path("hello/", HelloView.as_view(), name='hello')

]
urlpatterns = format_suffix_patterns(urlpatterns)
