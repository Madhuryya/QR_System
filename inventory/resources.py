from import_export import resources
from .models import Stock

class StockResource(resources.ModelResource):
    class meta:
        model=Stock