from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):

    course_title =serializers.ReadOnlyField()

    class Meta:
        model = Student
        fields = ['id', 'course', 'course_title', 'name', 'email', 'phone']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'