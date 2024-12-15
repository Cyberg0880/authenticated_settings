from rest_framework import serializers
from apps.users.models import User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone', 'full_name', 'is_superuser', 'is_staff')
