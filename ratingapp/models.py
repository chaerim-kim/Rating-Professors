from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Professor(models.Model):
    professor_id = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return u'%s %s %s' % (self.professor_id, self.first_name, self.last_name)


class Module(models.Model):
    module_code = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    semester = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)])
    taught_by = models.ManyToManyField(Professor)

    def __str__(self):
        return u'%s %s %d %d %s' % (self.module_code, self.name, self.year, self.semester, self.taught_by)


class Rating(models.Model):
    by_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating')  # for reverse relationship
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    which_professor = models.ForeignKey(Professor, on_delete=models.CASCADE,
                                        related_name='professor')
    which_module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='module')
