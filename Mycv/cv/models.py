from django.db import models

class Cv(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  phone = models.CharField(default=None, blank=True, null=True,max_length=255)
  summary = models.TextField()
  skills = models.TextField()
  experience = models.TextField()
  education = models.TextField()
  joined_date = models.DateField(default=None, blank=True, null=True)


  def __str__(self):
    return f"{self.name} {self.email} {self.phone}"