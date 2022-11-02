from rest_framework import serializers
from .models import Book
from django.forms import IntegerField, ValidationError


# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     number_of_pages = serializers.IntegerField()
#     publish_date = serializers.DateField()
#     quantity = serializers.IntegerField()

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


   
    def validate(self, data):
        if data['number_of_pages'] > 300 and data['quantity'] > 500:
            raise ValidationError('too veavy for inventory')
        return data