from django.db import models


class customManager(models.Manager):
    def get_queryset1(self):
        return super().get_queryset().order_by('esal')
    def get_emp_range(self,range1,range2):
        return super().get_queryset().filter(esal__range=(range1,range2)).order_by('esal')
    def get_emp_sorted(self,param):
        return super().get_queryset().order_by(param)

class employee(models.Model):
    ename=models.CharField(max_length=20)
    eno=models.IntegerField()
    esal=models.IntegerField()
    ecity=models.CharField(max_length=20)
    objects=customManager()
