from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import User

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only= True)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)
    class Meta:
        model = User
        fields = ['id','username','full_name','first_name','last_name', 'email','password','role', 'updated_at']
        extra_kwargs = {
            "first_name": {"write_only": True},
            "last_name": {"write_only": True},
            "password":{"write_only": True}
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    
    
    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        if user.role:
            try:
                group = Group.objects.get(name=user.role)
                user.groups.add(group)
            except Group.DoesNotExist:
                raise serializers.ValidationError({"role": f"Group for role '{user.role}' does not exist."})

        return user
