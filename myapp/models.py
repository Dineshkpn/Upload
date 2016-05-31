from django.db import models

class Document(models.Model):
	docfile = models.FileField(upload_to='documents')
	title = models.CharField(max_length=200)
	description = models.TextField()
