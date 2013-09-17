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
from django.template.defaultfilters import slugify

def post_pre_save(signal, instance, sender, **kwargs):
	if not instance.slug:
		slug = slugify(instance.title)
		new_slug = slug
		counter = 0

		while Post.objects.filter(slug=new_slug).exclude(id=instance.id).count() > 0:
			counter += 1
			new_slug = '%s-%d'%(slug, counter)

		instance.slug = new_slug

signals.pre_save.connect(post_pre_save, sender=Post)
