import pandas as pd
from django.core.management.base import BaseCommand
from actors.models import Actors


class Command(BaseCommand):

    def handle(self, *args, **options):
        actors = Actors.objects.all()
        actors_df = pd.DataFrame(list(actors.values()))
        actors_df['birthday'] = pd.to_datetime(actors_df['birthday'])
        actors_df['birthday'] = actors_df['birthday'].dt.strftime('%d/%m/%Y')

        for name in actors_df['name']:
            self.stdout.write(self.style.NOTICE(name))

        paste = (r'C:\\Users\\pedro\\flix-api\\')
        file_name = 'actors.xlsx'
        select = paste + file_name
        actors_df.to_excel(select, index=False)

        self.stdout.write(self.style.SUCCESS('ATORES EXPORTADOS COM SUCESSO'))
