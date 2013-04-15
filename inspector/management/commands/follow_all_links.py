from django.core.management.base import BaseCommand

from inspector.models import Inspection

class Command(BaseCommand):
    help = 'Follows all links in a site recursively'         

    def handle(self, *args, **options):
                
        inspection = Inspection(start_path="/")
        inspection.start_inspection()
        
        print "This was inspection:", inspection.id