from django.db import models
from django.contrib.auth.models import User


# so use manytomany when, both the one u are referencing and being referenced to
# can have many values
# use foreignkey WHEN the thing u are referecing by, cna have 1 foreignkey value

class Professor(models.Model):
    professor_id = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Module(models.Model):
    module_code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100)
    taught_by = models.ForeignKey(Professor, on_delete=models.CASCADE,
                                  related_name='taught_professor')
    year = models.IntegerField()
    semester = models.IntegerField()


class Rating(models.Model):
    by_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating')  # for reverse relationship
    rating = models.IntegerField()
    which_professor = models.ForeignKey(Professor, on_delete=models.CASCADE,
                                        related_name='professor')
    which_module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='module')
