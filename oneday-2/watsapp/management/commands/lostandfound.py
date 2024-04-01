import re
from urllib.request import urlopen

from django.core.management.base import BaseCommand
from watsapp.models import Case, Found, News


class Command(BaseCommand):
    help = "Найти информацию"


    def handle(self, *args, **options):
        count = 0

        for case in Case.objects.all():
            print(case)
            try:
                data = urlopen(case.url).read().decode('utf8')
                text = re.findall(case.pattern, data)[0]
            except Exception as e:
                continue

            old_found = Found.objects.filter(case=case).order_by('-created').first()
            if old_found:
                if old_found.text != text:
                    n = News(case=case, oldtext=old_found.text, newtext=text)
                    n.save()

            found = Found(case=case, text=text)
            found.save()

            count += 1

        self.stdout.write(
            self.style.SUCCESS('Successfully found: %s.' % count)
        )


