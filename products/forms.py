from django import forms

from products.models import Product, ProductPicture


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "single-input", "placeholder": "Full Name"}),
            "category": forms.Select(attrs={"class": " single-input"}),
            "brand": forms.Select(attrs={"class": "single-input"}),
            "count": forms.NumberInput(attrs={"class": "single-input", "placeholder": "Product Count"}),
            "price": forms.NumberInput(attrs={"class": "single-input", "placeholder": "Product Price"}),
            "is_available": forms.NullBooleanSelect(attrs={"class": "single-input"}),
            "sex": forms.Select(attrs={"class": "single-input"}),
            "description": forms.Textarea(attrs={"class": "single-input", "placeholder": "Product Description"}),
        }


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "single-input", "placeholder": "Full Name"}),
            "category": forms.Select(attrs={"class": " single-input"}),
            "brand": forms.Select(attrs={"class": "single-input"}),
            "count": forms.NumberInput(attrs={"class": "single-input", "placeholder": "Product Count"}),
            "price": forms.NumberInput(attrs={"class": "single-input", "placeholder": "Product Price"}),
            "is_available": forms.NullBooleanSelect(attrs={"class": "single-input"}),
            "sex": forms.Select(attrs={"class": "single-input"}),
            "description": forms.Textarea(attrs={"class": "single-input", "placeholder": "Product Description"}),
        }


class ProductPictureForm(forms.ModelForm):
    class Meta:
        model = ProductPicture
        fields = "__all__"


ProductFormSet = forms.inlineformset_factory(parent_model=Product, model=ProductPicture, form=ProductPictureForm,
                                             formset=forms.BaseInlineFormSet, fields="__all__", extra=4, max_num=4,
                                             can_delete_extra=True)
