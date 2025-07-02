from django.urls import path
from cbviews.crudviews import *


urlpatterns=[
    path('adduser/', Adduser.as_view()),
    path('users/', ListUser.as_view()),
    path('users/add/', Adduser.as_view()),
    path('users/<int:pk>/',DetailUser.as_view()),
    path('users/<int:pk>/edit',UpdateUser.as_view()),
    path('users/<int:pk>/delete/',DeleteUser.as_view()),
]


