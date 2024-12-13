from celery import shared_task
from .models import Product
import pandas as pd


@shared_task
def import_products_from_excel(file_path):
    data = pd.read_excel(file_path)
    for _, row in data.iterrows():
        Product.objects.get_or_create(name=row['name'], amount=row['amount'])
        