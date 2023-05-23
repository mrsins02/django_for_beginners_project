from django import forms

from products.models import Product


class ProductCreateForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "single-input", "placeholder": "Full Name"}),
            "category": forms.Select(attrs={"class":" single-input"}),
            "brand": forms.Select(attrs={"class": "single-input"}),
            "count": forms.NumberInput(attrs={"class": "single-input", "placeholder": "Product Count"}),
            "price": forms.NumberInput(attrs={"class": "single-input", "placeholder": "Product Price"}),
            "is_available": forms.NullBooleanSelect(attrs={"class": "single-input"}),
            "sex": forms.Select(attrs={"class": "single-input"}),
            "description": forms.Textarea(attrs={"class": "single-input", "placeholder": "Product Description"}),
        }




