from rest_framework import serializers
from .models import Tasks_list

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks_list
        exclude =('creation_date', 'last_update_date')