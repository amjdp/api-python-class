from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=500)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = 'student'


# {
# "student_name" : "athira",
# "age" : 24,
# "gender" : "Female",
# "email" : "athiramj@gmail.com",
# "phone" : 9823456785,
# "username" : "blah",
# "password" : "123456"
# }