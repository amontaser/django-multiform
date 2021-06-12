from .models import Address, Office
from bootstrap_modal_forms.forms import  BSModalModelForm 

class AddressForm(BSModalModelForm):
    class Meta:
        model = Address
        fields = ['address_line','address_line2','postal_code','notes','country','province','district']
    
    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    

class OfficeForm(BSModalModelForm):
    class Meta:
        model = Office
        fields = ['name','email']

    def __init__(self, *args, **kwargs):
        super(OfficeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'