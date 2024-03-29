import uuid
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.auth import get_user_model

class Category(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)
    slug = models.SlugField(null=True, unique=True)
    

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('phoneshop:products_by_category', args=[self.slug])

    def __str__(self):
        return self.name    

class Product(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    image_thumbnail = ImageSpecField(source='image',
                                processors=[ResizeToFill(180, 180)],
                                format='JPEG',
                                options={'quality': 60})
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    slug = models.SlugField(null=True, unique=True)#
    

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('phoneshop:prod_detail', args=[str(self.category.slug), str(self.slug)])

    def __str__(self):
        return self.name

class Comment(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse('product_list')

    




