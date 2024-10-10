from rest_framework import serializers
from users.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password


class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "password", "email"]

    def validate(self, attrs):
        if User.objects.filter(username=attrs["username"]).exists():
            raise serializers.ValidationError({"username": "Username already exists"})
        return attrs

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)
