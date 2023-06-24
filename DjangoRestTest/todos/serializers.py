from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    #title = serializers.CharField(allow_blank=True)
    #title = serializers.CharField(trim_whitespace=True)
    #title = serializers.CharField(max_length=100,min_length=10)

    def validate(self, data):
        title = data.get('title')
        body = data.get('body')
        if "$" in title or "$" in body:
            raise serializers.ValidationError("El titulo y el body no puede contener el simbolo $")
        return data
    
    # def validate_title(self, value):
    #     if "$" in value:
    #         raise serializers.ValidationError("El titulo no puede contener el simbolo $")
    #     return value
    
    # def validate_body(self,value):
    #     if "$" in value:
    #         raise serializers.ValidationError("El body no puede contener el simbolo $")
    #     return value

    def validate_status(self,value):
         if value not in [0,1,2,3]:
             raise serializers.ValidationError("El status solo puede tener de valores a 0,1,2,3")
         return value

    class Meta:
        model = Todo
        fields = (
            "id", "title", "body", "created_at",
            "done_at", "updated_at", "delete_at",
            "status",
        )

        read_only_fields = (
            "created_at","done_at", "updated_at", 
            "delete_at",
        )

class TestTodoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    body = serializers.CharField(max_length=200)
    status = serializers.IntegerField()

    def create(self,validated_data):
        return Todo(**validated_data)
    
    def update(self,instance,validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.body = validated_data.get('body',instance.body)
        instance.status = validated_data.get('status',instance.status)
        return instance
    

class TestValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            "name", "email", "url", "file_path",
            "ip", "integer", "float","decimal",
            "date","time","time_now"
        )