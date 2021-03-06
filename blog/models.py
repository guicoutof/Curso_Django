from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey("auth.User",on_delete=models.CASCADE)
	text = models.TextField(verbose_name='texto do blog')
	image = models.ImageField(upload_to='images', null=True, blank=True)
	slug = AutoSlugField(populate_form='tiltle',unique=True)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return '{} - {}'.format(self.title,self.author)