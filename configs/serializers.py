from rest_framework import serializers

from configs.models import Config, User
from users.serializers import UserPublicSerializer

class ConfigSerializer(serializers.ModelSerializer):
    author = UserPublicSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='author',
        write_only=True
    )
    
    class Meta:
        model = Config
        fields = ['id', 'name', 'description', 'file', 'author','author_id', 'creation_date', 'tags']
