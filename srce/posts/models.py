from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
#model utilisateur de base de django
user = get_user_model()
# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='titre')
    slug = models.SlugField(max_length=255, unique=True,blank=True)
    author = models.ForeignKey(user, on_delete=models.SET_NULL, null=True, blank=True)
    #enregistre avec la date actuel automatiquement
    last_update = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name='publié')
    content = models.TextField(blank=True, verbose_name='contenu')
    image = models.ImageField(blank=True, upload_to='blog')

    class Meta:
        #ordoner inversement de created_on
        ordering = ['-created_on']
        verbose_name = 'article'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def author_or_default(self):
        if self.author:
            return self.author.username
        return "L'auteur inconnu"

#redirection absolue
    def get_absolute_url(self):
        return reverse('posts:home')