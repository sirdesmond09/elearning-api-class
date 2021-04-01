from django.urls import path
from .views import *

urlpatterns = [
    path('students/', students),
    path('student/<int:student_id>/', get_student),
    path('courses/', courses),
    path('course/<int:course_id>/', get_course)
]
