from rest_framework import serializers
from demo.models import Demo_model

class DemoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Demo_model 
    fields = '__all__'
