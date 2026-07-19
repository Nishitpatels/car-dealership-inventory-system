from django import forms


class PurchaseForm(forms.Form):
    vehicle_id = forms.IntegerField(min_value=1)
    quantity = forms.IntegerField(min_value=1, initial=1)

    def clean_quantity(self):
        quantity = self.cleaned_data["quantity"]
        if quantity <= 0:
            raise forms.ValidationError("Purchase quantity must be greater than zero.")
        return quantity
