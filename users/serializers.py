from rest_framework import serializers
from users.models import EndUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndUser
        fields = ['first_name','last_name','company_name','city','state','web','zip','age','email']
