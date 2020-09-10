from django.db import models

# Create your models here.
class users(models.Model):
    u_name = models.CharField(max_length = 30)
    u_pwd = models.CharField(max_length = 30)
    u_type = models.CharField(max_length = 10)

    def __str__(self):
        return self.u_name

class leave_application(models.Model):
    e_id = models.CharField(max_length=10)
    e_name = models.CharField(max_length=30)
    e_desig = models.CharField(max_length=30)
    e_application = models.CharField(max_length=500)
    f_date = models.DateTimeField('date published')
    t_date = models.DateTimeField('date published')
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.e_name