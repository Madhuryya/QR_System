from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View,
    CreateView, 
    UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Stock
from .forms import StockForm
from django_filters.views import FilterView
from .filters import StockFilter
from django.views.generic import DetailView
from .forms import StockForm
from .resources import StockResource
from tablib import Dataset

class StockListView(FilterView):
    filterset_class = StockFilter
    queryset = Stock.objects.filter(is_deleted=False)
    template_name = 'inventory.html'
    paginate_by = 10


class StockCreateView(SuccessMessageMixin, CreateView):                                 # createview class to add new stock, mixin used to display message
    model = Stock                                                                       # setting 'Stock' model as model
    form_class = StockForm                                                              # setting 'StockForm' form as form
    template_name = "edit_stock.html"                                                   # 'edit_stock.html' used as the template
    success_url = '/inventory'                                                          # redirects to 'inventory' page in the url after submitting the form
    success_message = "Stock has been created successfully"                             # displays message when form is submitted

    def post(self,request):
        form=StockForm(self.request.POST)
        if form.is_valid():
            print(form.data)
            form.save() 
        else:
            return HttpResponse(content='error')
        
        
        
    def get_context_data(self, **kwargs):                                               # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'New Stock'
        context["savebtn"] = 'Add to Inventory'
        return context    
    

class StockUpdateView(SuccessMessageMixin, UpdateView):                                 # updateview class to edit stock, mixin used to display message
    model = Stock                                                                       # setting 'Stock' model as model
    form_class = StockForm                                                              # setting 'StockForm' form as form
    template_name = "edit_stock.html"                                                   # 'edit_stock.html' used as the template
    success_url = '/inventory'                                                          # redirects to 'inventory' page in the url after submitting the form
    success_message = "Stock has been updated successfully"                             # displays message when form is submitted

    def get_context_data(self, **kwargs):                                               # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit Stock'
        context["savebtn"] = 'Update Stock'
        context["delbtn"] = 'Delete Stock'
        return context
    
    


class StockDeleteView(View):                                                            # view class to delete stock
    template_name = "delete_stock.html"                                                 # 'delete_stock.html' used as the template
    success_message = "Stock has been deleted successfully"                             # displays message when form is submitted
    
    def get(self, request, pk):
        stock = get_object_or_404(Stock, pk=pk)
        return render(request, self.template_name, {'object' : stock})

    def post(self, request, pk):  
        stock = get_object_or_404(Stock, pk=pk)
        stock.is_deleted = True
        stock.save()                                               
        messages.success(request, self.success_message)
        return redirect('inventory')
    
def audit_stock(request):
    # Your view logic for auditing stocks
    return render(request, 'audit_stock.html')



class StockDetailView(SuccessMessageMixin, DetailView):
    model = Stock
    form_class = StockForm
    template_name = "read.html"
    success_url = '/inventory'
    success_message = "Stock has been updated successfully"

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'View Stock'
        context["savebtn"] = 'Audit Stock'
        return context
    
def simple_upload(request):
    print(request.FILES)  # Print request.FILES
    print(request.POST)

    if request.method == 'POST':
        stock_resource = StockResource()
        dataset = Dataset()
        new_stock = request.FILES['myfile']

        if not new_stock.name.endswith('xlsx'):
            messages.error(request, 'Wrong format. Please upload an Excel file.')
            return redirect('upload')  # Redirect back to the upload page on error

        try:
            imported_data = dataset.load(new_stock.read(), format='xlsx')
            
            for data in imported_data:
                quantity_str = data[3]
                quantity_value = int(quantity_str[1:-1]) if quantity_str.startswith('(') and quantity_str.endswith(')') else int(quantity_str)
                value = Stock(
                   data[0],  # Replace with the correct index based on your data structure
                   data[1],
                   data[2],
                   data[3],
                   data[4],
                   data[5],
                   data[6],
                   data[7],
                    # Repeat for other fields...
                )
                value.save()

            messages.success(request, 'Stocks have been imported successfully.')
            return redirect('upload')  # Redirect to the upload page after successful import

        except Exception as e:
            messages.error(request, f'Error importing stocks: {str(e)}')
            return redirect('upload')  # Redirect back to the upload page on error

    # Handle GET request
    return render(request, 'upload.html')
