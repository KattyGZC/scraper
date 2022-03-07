from django.core.management.base import BaseCommand, CommandError
from scraper_pe.processor import process_data
import time
import os

class Command(BaseCommand):
    help = 'Data processing'

    def add_arguments(self, parser):
        try:
            parser.add_argument('filename', nargs='+', type=str)
        except Exception as error:
            raise CommandError(f'Ups! Algo salió mal: {error}')

    def handle(self, *args, **options):
        try:
            init_hour = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            print(f'Iniciando proceso... \n{init_hour}\n')
            if os.path.isfile(options['filename'][0]) and os.path.exists(options['filename'][0]):
                print('Procesando datos...')
                process_data(options['filename'][0])
            else:
                self.stderr.write(self.style.ERROR('No existe el archivo...'))
    
            finish_hour = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            print(f'Proceso finalizado... \n{finish_hour}\n') 
        except Exception as error:
            raise CommandError(f'Ups! Algo salió mal: {error}')