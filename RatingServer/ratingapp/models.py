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
        taught_by = ", ".join(str(seg) for seg in self.taught_by.all())
        return u'%s %s %d %d' % (self.module_code, taught_by, self.year, self.semester)


class Rating(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    which_professor = models.ForeignKey(Professor, on_delete=models.CASCADE )
    which_module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return u'%s %s %s' % (self.rating, self.which_professor.professor_id, self.which_module.module_code)
