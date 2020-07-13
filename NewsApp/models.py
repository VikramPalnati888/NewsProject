from django.db import models

class News(models.Model):
	Title = models.CharField(max_length=100, null=True)
	Description = models.TextField()
	Image = models.ImageField(null=True, blank=True)
	Likes = models.IntegerField(blank=True,null=True, default=0)
	PostedDate = models.DateTimeField(auto_now_add=True, blank=True)
	
	def __str__(self):
		return "%s" %(self.Title)
