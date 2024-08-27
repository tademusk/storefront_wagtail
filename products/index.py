from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Product

@register(Product)
class ProductIndex(AlgoliaIndex):
    fields = ('title', 'description', 'price', 'rating', 'views')
    settings = {'searchableAttributes': ['title', 'description']}
    index_name = 'products'
