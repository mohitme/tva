from rest_framework import serializers
from users.models import EndUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndUser
        fields = "__all__"
