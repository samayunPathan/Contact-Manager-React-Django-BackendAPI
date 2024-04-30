from rest_framework.serializers import ModelSerializer
from contactAPI.models import UserProfile,Contact

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model=UserProfile
        fields=(
            "id",
            "email",
            "password",
        )
        extra_kwargs={
            "password":{"write_only":True,"style":{"input_style":"password"}}
        }

    def create(self, validated_data):
        user=UserProfile.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user
    
class ContactSerializer(ModelSerializer):
   
    class Meta:
        model=Contact
        fields="__all__"