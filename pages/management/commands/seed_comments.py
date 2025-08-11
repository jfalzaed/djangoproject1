from django.core.management.base import BaseCommand
from pages.models import Comment, Product
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Crea comentarios de ejemplo para productos existentes'

    def handle(self, *args, **kwargs):
        products = Product.objects.all()

        if not products.exists():
            self.stdout.write(self.style.ERROR('No hay productos en la base de datos. Crea productos primero.'))
            return

        for _ in range(5):  # cantidad de comentarios que quieres crear
            product = random.choice(products)
            Comment.objects.create(
                product=product,
                description=fake.sentence()
            )

        self.stdout.write(self.style.SUCCESS('Se crearon comentarios de ejemplo correctamente'))
