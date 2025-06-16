from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site

class Command(BaseCommand):
    help = 'Update site domain for password reset emails'

    def handle(self, *args, **options):
        site, created = Site.objects.get_or_create(pk=1)
        site.domain = 'symphonious-licorice-91a25d.netlify.app'
        site.name = 'AumOui Lifestyle Essentials'
        site.save()
        
        if created:
            self.stdout.write(f'Created new site: {site.domain}')
        else:
            self.stdout.write(f'Updated site domain to: {site.domain}')
        
        self.stdout.write(self.style.SUCCESS('Site updated successfully!'))
