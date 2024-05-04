from rest_framework.viewsets import ModelViewSet
from contactAPI.models import UserProfile,Contact
from contactAPI.serializers import UserProfileSerializer,ContactSerializer

# Create your views here.
class UserProfileViewSet(ModelViewSet):
    serializer_class=UserProfileSerializer
    queryset=UserProfile.objects.all()

class ContactViewSet(ModelViewSet):
    serializer_class=ContactSerializer
    queryset=Contact.objects.all()