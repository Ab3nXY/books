from django.core.management.base import BaseCommand
import pandas as pd
from quillcart.models import Book # Import your model

class Command(BaseCommand):
    help = 'Import data from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the Excel file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        df = pd.read_excel(file_path)  # Use read_csv for CSV files

        for _, row in df.iterrows():
            your_model_instance = Book(**row)
            your_model_instance.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully added data for {your_model_instance}'))
