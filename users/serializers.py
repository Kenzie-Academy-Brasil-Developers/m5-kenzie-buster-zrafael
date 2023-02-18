from rest_framework import serializers
from .models import Account
from rest_framework.validators import UniqueValidator


class RegisterSerializer(serializers.Serializer):
    
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        max_length=150,
        validators=[UniqueValidator(
            queryset=Account.objects.all(), message="username already taken."
            )],
    )
    email = serializers.EmailField(
        max_length=127,
        validators=[UniqueValidator(
            queryset=Account.objects.all(), message="email already registered."
        )],
    )
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(allow_null=True, default=None)
    is_employee = serializers.BooleanField(allow_null=True, default=False)
    password = serializers.CharField(write_only=True)
    is_superuser = serializers.BooleanField(allow_null=True, default=False)

    def create(self, validated_data):
        if validated_data['is_employee'] == True or validated_data['is_employee'] == 1:
            validated_data['is_superuser'] = validated_data['is_employee']
            return Account.objects.create_superuser(**validated_data)
        return Account.objects.create_user(**validated_data)
    
    def update(self, instance: Account, validated_data: dict):

        for key, value in validated_data.items():
            
            if key == 'password':
                instance.set_password(value)
            else:
                setattr(instance, key, value)
        
        instance.save()
        return instance

