from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.users.models import User
from apps.users.serializers import UserDetailSerializer
from apps.users.authentication import BasicAuthentication


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]



