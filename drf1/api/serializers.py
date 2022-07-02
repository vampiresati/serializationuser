from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=40)
    roll_number = serializers.IntegerField()