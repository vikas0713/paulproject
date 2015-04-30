from django import forms
from models import OrderModel, DriverModel
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div
from datetimewidget.widgets import DateTimeWidget

class OrderForm(forms.ModelForm):
    
    
    
    class Meta:
        model= OrderModel
        exclude=[]
        dateTimeOptions = {'format': 'yyyy/mm/dd', 'autoclose': True,'showMeridian' : True}
#        widgets = {
#            #Use localization and bootstrap 3
#            'datetime': DateTimeWidget(attrs={'id':"datetime"}, usel10n = True, bootstrap_version=3)
#        }
    def __init__(self , *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['del_date'].widget.attrs.update({'id':'datepicker'})
        self.fields['ship_date'].widget.attrs.update({'id':'datepicker1'})
    
class DriverForm(forms.ModelForm):
    
    class Meta:
        model= DriverModel
        exclude=[]
        
    def __init__(self, *args, **kwargs):
        super(DriverForm, self).__init__(*args, **kwargs)
        self.fields['dl_expiry'].widget.attrs.update({'id':'datepicker'})