from rest_framework import serializers
from .models import Course, CourseInstance

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'course_code', 'description']


class CourseInstanceSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)  # Nested serializer for read operations
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        source='course',  # This maps 'course_id' to 'course' field in the model
        write_only=True   # Write-only so it's not included in serialized output
    )

    class Meta:
        model = CourseInstance
        fields = ['id', 'course', 'course_id', 'year', 'semester']
