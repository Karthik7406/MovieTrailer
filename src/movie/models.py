from django.db import models
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.

CATEGORY_CHOICES = (
    ('action', 'ACTION'),
    ('drama', 'DRAMA'),
    ('comedy', 'COMEDY'),
    ('romance', 'ROMANCE')
)

LANGUAGE_CHOICES = (
    ('EN', 'ENGLISH'),
    ('HI', 'HINDI'),
    ('KA', 'KANNADA'),
    ('TE', 'TELUGU'),
    ('TN', 'TAMIL')
)

STATUS_CHOICES = (
    ('RA', 'RECENTLY ADDED'),
    ('MW', 'MOST WATCHED'),
    ('TR', 'TOP RATED')
)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='movies')
    banner = models.ImageField(upload_to='movies_banner')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    year_of_production = models.DateField()
    views_count = models.IntegerField(default=0)
    cast = models.CharField(max_length=100)

    created = models.DateTimeField(default=timezone.now)

    # slug feild is used in the url to access with the help of the title instead of name
    slug = models.SlugField(blank=True, null=True)

    movie_trailer = models.URLField()



    def save(self, *args, **kwargs):
        # if there is no slug add a slug
        if not self.slug:
            self.slug = slugify(self.title)
        super(Movie, self).save( *args, **kwargs)

    def __str__(self):
        return self.title


# -add watch links and download links to the model

LINK_CHOICES = (
    ('D', 'DOWNLOAD'),
    ('W', 'WATCH')
)


class MovieLink(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_watch_link', on_delete=models.CASCADE)
    type = models.CharField(choices=LINK_CHOICES, max_length=1)
    links = models.URLField()
