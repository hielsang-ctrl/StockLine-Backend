from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Create superuser from environment variables if it does not exist'

    def handle(self, *args, **kwargs):
        from decouple import config
        email = config('SUPERUSER_EMAIL', default='')
        password = config('SUPERUSER_PASSWORD', default='')
        username = config('SUPERUSER_USERNAME', default='admin')

        if not email or not password:
            self.stdout.write('SUPERUSER_EMAIL or SUPERUSER_PASSWORD not set, skipping.')
            return

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            user.set_password(password)
            user.is_staff = True
            user.is_superuser = True
            user.role = 'admin'
            user.save()
            self.stdout.write(f'Superuser {email} updated.')
            return

        user = User.objects.create_superuser(username=username, email=email, password=password)
        user.role = 'admin'
        user.save()
        self.stdout.write(self.style.SUCCESS(f'Superuser {email} created.'))
