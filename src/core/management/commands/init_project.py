# -*- coding: utf-8 -*-
"""
Init project.
"""

import logging
import random

from django.core.management import BaseCommand
from wagtail.users.views.users import User

from config import settings
from faker import Faker

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Command for basic data initialization.
    """

    faker: Faker = Faker("uk-UA")

    def handle(self, *args, **options) -> None:
        """
        Handle command.

        :param args:
        :param options:
        :return:
        """
        logger.info("Start Init project.")
        self._create_superuser()
        self._create_users()

    def _create_superuser(self) -> None:
        """
        Create superuser.
        """
        if not User.objects.filter(email=settings.ADMIN_EMAIL).exists():
            self.stdout.write(self.style.WARNING("Start creating superuser"))

            # create superuser
            User.objects.create_superuser(
                email=settings.ADMIN_EMAIL,
                username=settings.ADMIN_USERNAME,
                password=settings.ADMIN_PASSWORD,
                is_staff=True,
            )

            self.stdout.write(self.style.SUCCESS("Superuser created"))
        else:
            self.stdout.write(self.style.WARNING("Superuser already exists"))

    def _create_users(self) -> None:
        """
        Create users.
        """
        if not User.objects.filter(is_superuser=False).exists():
            self.stdout.write(self.style.WARNING("Start creating users"))
            # Init number of created users
            users_numbers: int = random.randint(5, 20)

            for index in range(users_numbers):
                user: User = User.objects.create(
                    email=settings.USER_EMAIL if index == 0 else self.faker.email(),
                    username=self.faker.user_name(),
                    is_superuser=False,
                )

                # set password
                user.set_password(settings.USER_PASSWORD)
                user.save()

            self.stdout.write(self.style.SUCCESS("User created"))
        else:
            self.stdout.write(self.style.WARNING("User already exists"))
