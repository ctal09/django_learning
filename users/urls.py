from django.urls import path
from users.views import education, experience
urlpatterns = [
    path('education/', education),
    path('experience/', experience),
]