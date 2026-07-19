from django import forms

from .models import Vehicle


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ["make", "model", "category", "price", "quantity", "description", "image"]

    def clean_make(self):
        return self.cleaned_data["make"].strip()

    def clean_model(self):
        return self.cleaned_data["model"].strip()

    def clean_description(self):
        return self.cleaned_data["description"].strip()

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price

    def clean_quantity(self):
        quantity = self.cleaned_data["quantity"]
        if quantity < 0:
            raise forms.ValidationError("Quantity cannot be negative.")
        return quantity

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if not image:
            return image

        allowed_types = {"image/jpeg", "image/png", "image/webp", "image/svg+xml"}
        content_type = getattr(image, "content_type", "")
        if content_type and content_type not in allowed_types:
            raise forms.ValidationError("Upload a JPG, PNG, WEBP, or SVG image.")

        max_size = 5 * 1024 * 1024
        if image.size > max_size:
            raise forms.ValidationError("Image size must be 5MB or less.")

        return image


class RestockForm(forms.Form):
    vehicle_id = forms.IntegerField(min_value=1)
    quantity = forms.IntegerField(min_value=1)

    def clean_quantity(self):
        quantity = self.cleaned_data["quantity"]
        if quantity <= 0:
            raise forms.ValidationError("Restock quantity must be greater than zero.")
        return quantity
