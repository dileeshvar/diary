from django.db import models

class Diary(models.Model):
	to_do_task = models.CharField(max_length=1000)
	task_date = models.DateTimeField('task date')
	
	def __unicode__(self):
		return self.to_do_task
