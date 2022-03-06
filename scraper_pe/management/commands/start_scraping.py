from django.core.management.base import BaseCommand, CommandError
from scraper_pe.processor import start_scraping
import time

class Command(BaseCommand):
    help = 'Inizialitation scraping'

    def handle(self, *args, **options):
        try:
            init_hour = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            print(f'Iniciando proceso... \n{init_hour}\n')
            print(f'Proporcione la siguiente información: ')
            content_type = input('Tipo de contenido: ')
            category = input('Categoria: ')
            format = input('Formato de descarga: ')
            report_name = input('Nombre del reporte: ')
            start_scraping(content_type, category, format, report_name)
        except Exception as error:
            raise CommandError(f'Ups! Algo salió mal: {error}')

        self.stdout.write(self.style.SUCCESS('Successfully...'))