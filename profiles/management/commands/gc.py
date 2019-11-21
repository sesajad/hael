from django.core.management.base import BaseCommand
from django.utils import timezone

from profiles.models import IpSpec
from profiles.helpers import remove_whitelist_ip


class Command(BaseCommand):
    help = 'Garbage Collection!'

    def handle(self, *args, **options):
        for ip in IpSpec.objects.all():
            if ip.expire_time < timezone.now():
                remove_whitelist_ip(ip.address)
                ip.delete()
                self.stdout.write(self.style.SUCCESS('Successfully deleted ip "%s"' % ip.address))
        self.stdout.write(self.style.SUCCESS('Job finished'))
