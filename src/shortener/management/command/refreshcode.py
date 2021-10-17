from django.core.management.base import BaseCommand, CommandError
from shortener.model import Kirurl

class Command(BaseCommand):
    help = 'Refresh Kirurl'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        
        return Kirurl.objects.refresh_shortcodes(items=options['items'])