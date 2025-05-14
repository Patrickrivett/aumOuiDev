from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password    = serializers.CharField(write_only=True)
    age_group   = serializers.CharField(required=False, allow_blank=True)
    hair_types  = serializers.ListField(
        child=serializers.CharField(), required=False, allow_empty=True
    )
    skin_types  = serializers.ListField(
        child=serializers.CharField(), required=False, allow_empty=True
    )
    allergies   = serializers.ListField(
        child=serializers.CharField(), required=False, allow_empty=True
    )

    class Meta:
        model  = User
        fields = (
            'username',
            'email',
            'password',
            'age_group',
            'hair_types',
            'skin_types',
            'allergies',
        )

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = (
            'id',
            'username',
            'email',
            'age_group',
            'hair_types',
            'skin_types',
            'allergies',
        )
