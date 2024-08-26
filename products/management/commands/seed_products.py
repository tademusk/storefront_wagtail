from django.core.management.base import BaseCommand
from wagtail.models import Page
from products.models import Product

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        parent_page = Page.objects.get(slug='products')
        for i in range(1, 11):
            product = Product(
                title=f'Product {i}',
                description='This is the description for product {i}',
                price=10.00 + i,
                rating=4.5,
            )
            parent_page.add_child(instance=product)
            product.save()
        self.stdout.write(self.style.SUCCESS('Successfully seeded products'))
