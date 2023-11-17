from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(email = validated_data['email'],password = validated_data['password'],is_staff=False,is_superuser=False)
        return user

    '''
    TypeError: UserManager.create_user() missing 2 required positional arguments: 'is_staff' and 'is_superuser'
    '''