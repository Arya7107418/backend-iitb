from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Course, CourseInstance
from .serializers import CourseSerializer, CourseInstanceSerializer

# List and create courses
class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# Retrieve and delete a specific course
class CourseDetail(generics.RetrieveDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# Create a new course instance
class CourseInstanceCreate(generics.CreateAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

# List course instances for a specific year and semester
class CourseInstanceList(generics.ListAPIView):
    serializer_class = CourseInstanceSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        return CourseInstance.objects.filter(year=year, semester=semester)

# Retrieve a specific course instance
class CourseInstanceDetail(generics.RetrieveAPIView):
    serializer_class = CourseInstanceSerializer

    def get_object(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        course_id = self.kwargs['course_id']
        return get_object_or_404(CourseInstance, year=year, semester=semester, course__id=course_id)

# Delete a specific course instance
class CourseInstanceDelete(generics.DestroyAPIView):
    serializer_class = CourseInstanceSerializer

    def get_object(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        course_id = self.kwargs['course_id']
        return get_object_or_404(CourseInstance, year=year, semester=semester, course__id=course_id)
