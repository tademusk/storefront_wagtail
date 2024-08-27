import json
from django.core.management.base import BaseCommand
from wagtail.models import Page
from products.models import Product
from decimal import Decimal, InvalidOperation

class Command(BaseCommand):
    help = 'Seed the Product model with data from products.json'

    def handle(self, *args, **kwargs):
        try:
            with open('products/fixtures/products.json') as file:
                products_data = json.load(file)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('File products/fixtures/products.json not found.'))
            return
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Error decoding JSON file.'))
            return

        try:
            parent_page = Page.objects.get(slug='product')
        except Page.DoesNotExist:
            self.stdout.write(self.style.ERROR('Parent page with slug "product" does not exist.'))
            return

        for product_data in products_data:
            try:
                price = Decimal(product_data['price']).quantize(Decimal('0.01')) 
            except (InvalidOperation, ValueError):
                self.stdout.write(self.style.ERROR(f"Invalid price value for product: {product_data['title']}"))
                continue

            product = Product(
                title=product_data['title'],
                description=product_data['description'],
                price=price,
                rating=product_data['rating'],
                views=product_data['views'],
                live=True
            )
            parent_page.add_child(instance=product)
            product.save()

        self.stdout.write(self.style.SUCCESS('Successfully seeded products.'))
