from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=300)
    code = models.CharField(max_length=10)
    desc = models.TextField()


class Student(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name   = models.CharField(max_length=300)
    email  = models.EmailField(unique=True)
    phone  = models.CharField(max_length=12)

    @property
    def course_title(self):
        return self.course.title




