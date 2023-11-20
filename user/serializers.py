from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        user = User.objects.create(
            email = validated_data['email'],
            password = validated_data['password'],
            )
        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['old_password', 'new_password']

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)