from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from utils.make_slug import make_slugify


class BaseModel(models.Model):
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Tag(BaseModel):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Blog(BaseModel):
    title = models.CharField(max_length=221)
    slug = models.SlugField(max_length=221)
    image = models.ImageField(upload_to='blog/')
    author = models.CharField(max_length=221, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)
    content = models.TextField()

    def __str__(self):
        return self.title


class Comment(BaseModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comment = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    top_level_comment_id = models.IntegerField(null=True, blank=True)

    @property
    def get_children(self):
        model = self.__class__
        return model.objects.filter(top_level_comment_id=self.id)


@receiver(pre_save, sender=Blog)
def article_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        make_slugify(instance)



def comment_pre_save(sender, instance, *args, **kwargs):
    if instance.parent:
        if not instance.parent.top_level_comment_id:
            instance.top_level_comment_id = instance.parent_id
        else:
            instance.top_level_comment_id = instance.parent.top_level_comment_id



pre_save.connect(comment_pre_save, sender=Comment)
