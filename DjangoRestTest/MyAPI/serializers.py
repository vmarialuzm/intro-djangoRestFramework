from rest_framework import serializers
from .models import Pais,Comment,User

class PaisSerializador(serializers.ModelSerializer):
  class Meta:
    model = Pais
    fields = ('nombre','moneda')


class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ('url','username','email',)


class CommentSerializer(serializers.Serializer):
   email = serializers.EmailField()
   content = serializers.CharField(max_length=200)
   created = serializers.DateTimeField()

   def create(self,validated_data):
     return Comment(**validated_data)
   
   def update(self,instance,validated_data):
     instance.email = validated_data.get('email',instance.email)
     instance.content = validated_data.get('content',instance.content)
     instance.created = validated_data.get('created',instance.created)
     return instance
   




