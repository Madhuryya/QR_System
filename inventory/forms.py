from django import forms
from .models import Stock

class StockForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):                                                        # used to set css classes to the various fields
        super().__init__(*args, **kwargs)
        self.fields['description_of_item'].widget.attrs.update({'class': 'textinput form-control'})
        # self.fields['img'].widget.attrs.update({'class': 'orm-control-file'})
        self.fields['location'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})

    class Meta:
        model = Stock
        fields = ['description_of_item', 'location','quantity','registration','status','remarks','po']
