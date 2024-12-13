from django.core.management.base import BaseCommand
from orders.tasks import import_products_from_excel

class Command(BaseCommand):
    def handle(self, *args, **options):
        file_path = 'path_to_your_excel_file.xlsx'
        import_products_from_excel.delay(file_path)
