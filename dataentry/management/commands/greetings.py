from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Prints a greeting message'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name of the person to greet')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        self.stdout.write(f'Hello, {name}!')    