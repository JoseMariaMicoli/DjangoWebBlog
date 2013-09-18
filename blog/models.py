from django.db import models
from taggit.managers import TaggableManager
from django.core.urlresolvers import reverse


# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	create = models.DateTimeField()
	tags = TaggableManager()
	slug = models.SlugField(max_length=100, blank=True, unique=True)

	def get_absolute_url(self):
		return reverse('blog.views.post', kwargs = {'slug': self.slug})

	def __unicode__(self):
		return self.title

# SIGNALS

from django.db.models import signals
from utils.signals_common import slug_pre_save

signals.pre_save.connect(slug_pre_save, sender=Post)
