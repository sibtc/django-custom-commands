from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Delete users'

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        users_ids = kwargs['user_id']

        for user_id in users_ids:
            try:
                user = User.objects.get(pk=user_id)
                user.delete()
                self.stdout.write(self.style.SUCCESS('User "%s (%s)" deleted with success!' % (user.username, user_id)))
            except User.DoesNotExist:
                self.stdout.write(self.style.WARNING('User with id "%s" does not exist.' % user_id))
