import os
import random

from django.conf import settings
from django.core.management.base import BaseCommand
from faker import Faker
from tickets.models import Ticket
from reviews.models import Review
from follows.models import UserFollows
from users.models import CustomUser
fake = Faker()


class Command(BaseCommand):
    help = 'Seed the database with sample data'
    def handle(self, *args, **kwargs):
        users = []
        user = CustomUser.objects.create_user(
            username="test_user",
            email=fake.email(),
            password="password123",
        )
        users.append(user)

        for i in range(4):
            user = CustomUser.objects.create_user(
                username=f"test_user_{i+2}",
                email=fake.email(),
                password="password123",
            )
            users.append(user)

        self.stdout.write(self.style.SUCCESS("5 utilisateurs créés"))

        tickets = []
        for _ in range(10):
            user = random.choice(users)
            ticket = Ticket.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.text(max_nb_chars=200),
                user=user,
                time_created=fake.date_this_year(),
                image=get_random_image(),
            )
            tickets.append(ticket)

        self.stdout.write(self.style.SUCCESS("10 tickets créés"))

        for ticket in tickets:
            if random.choice([True, False]):
                user = random.choice(users)
                review = Review.objects.create(
                    ticket=ticket,
                    rating=random.randint(1, 5),
                    user=user,
                    headline=fake.sentence(nb_words=5),
                    body=fake.text(max_nb_chars=300),
                )
                self.stdout.write(self.style.SUCCESS(f"Review pour le ticket {ticket.title} créée"))

        for user in users:
            followed_user = random.choice([u for u in users if u != user])
            UserFollows.objects.create(
                user=user,
                followed_user=followed_user,
            )

        self.stdout.write(self.style.SUCCESS("Abonnements au hasard créés."))


def get_random_image():
    media_path = os.path.join(settings.MEDIA_ROOT, "tickets_images")
    images = [f for f in os.listdir(media_path) if os.path.isfile(os.path.join(media_path, f))]


    random_image = random.choice(images)
    return os.path.join(media_path, random_image)
