from django.template.defaultfilters import slugify

def slug_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        slug = slugify(instance.title)
        new_slug = slug
        counter = 0

        while sender.objects.filter(slug=new_slug).exclude(id=instance.id).count() >0:
            counter += 1
	    new_slug = '%s-%d'%(slug, counter)
