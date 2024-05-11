from django.db import models

class Folder(models.Model):
  data_created = models.DateTimeField(auto_now_add=True) 
  data_updated = models.DateTimeField(auto_now=True) 

  # main
  name = models.CharField(max_length=200)
  def __str__(self):
    return self.name

class Note(models.Model):
  data_created = models.DateTimeField(auto_now_add=True) 
  data_updated = models.DateTimeField(auto_now=True) 

  # main
  folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, blank=True)
  title = models.CharField(max_length=200)
  content = models.TextField(null=True, blank=True)

  def __str__(self):
    return self.title

