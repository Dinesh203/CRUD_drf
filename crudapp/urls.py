
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from crudapp.views import UserDetail, UserUpdate

urlpatterns = [
    path("APIview/", UserDetail.as_view()),
    path("update_user/<int:pk>/", UserUpdate.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
