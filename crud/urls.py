from django.urls import path
from .views import *

urlpatterns = [
    path('users/', users_list),
    path('users/<int:id>/user-detail/', user_detail),
    path('users/add',add_user),
    path('users/<int:id>/delete/',delete_user)
    
    ]