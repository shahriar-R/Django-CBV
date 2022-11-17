from unittest.util import _MAX_LENGTH
from rest_framework import serializers

from ...models import Post


#class PostSerializer(serializers.Serializer):
#    tiitle = serializers.CharField(_max_length=255)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','content','status','create_date']
