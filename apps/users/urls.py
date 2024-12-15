from django.urls import path
from apps.users.views import UserDetailView

urlpatterns = [
    path('<int:pk>', UserDetailView.as_view()),
]