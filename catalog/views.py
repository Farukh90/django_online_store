from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


from catalog.forms import ProductForm, VersionForm
from catalog.utils import read_JSON_data
from catalog.utils import write_JSON_data
from catalog.utils import create_contact_dict
from catalog.models import Category, Product, Version

contacts_base_file = r"contacts.json"


class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "product_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for product in context["product_list"]:
            product.active_version = product.versions.filter(is_current=True).first()
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:products_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:products_list")

    def get_success_url(self):
        return reverse_lazy("catalog:product_update", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(
            Product, Version, form=VersionForm, extra=1
        )

        if self.request.method == "POST":
            context_data["formset"] = ProductFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = ProductFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()["formset"]
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:products_list")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return redirect(success_url)



class ContactView(View):
    template_name = "catalog/contacts.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name} ({email}): {message}")

        new_contact = create_contact_dict(name, email, message)

        contacts_base = read_JSON_data(contacts_base_file)

        contacts_base.append(new_contact)

        write_JSON_data(contacts_base_file, contacts_base)

        return render(request, self.template_name)
