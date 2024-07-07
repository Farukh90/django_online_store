from django.forms import ModelForm, forms
from catalog.models import Product, Version


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    forbidden_words = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        for word in self.forbidden_words:
            if word in name.lower():
                raise forms.ValidationError(
                    f"Название продукта не может содержать слово: {word}"
                )
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        for word in self.forbidden_words:
            if word in description.lower():
                raise forms.ValidationError(
                    f"Описание продукта не может содержать слово: {word}"
                )
        return description


class VersionForm(ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
