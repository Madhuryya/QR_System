from django.contrib import admin
from .models import Stock
from import_export.admin import ImportExportModelAdmin

admin.site.register(Stock)

class StockAdmin(ImportExportModelAdmin):
    list_display=('id','description_of_item','po','quantity','location','registration','status','remarks')


#new edit


