from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.search import index

class Product(Page):
    description = RichTextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    views = models.IntegerField(default=0)

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('description'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('price'),
        FieldPanel('rating'),
        FieldPanel('views'),
    ]

class ProductsIndexPage(Page):
    name = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('name')
    ]
