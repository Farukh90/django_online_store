from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView

from catalog.utils import read_JSON_data
from catalog.utils import write_JSON_data
from catalog.utils import create_contact_dict
from catalog.models import Category, Product

contacts_base_file = r'contacts.json'


class ProductListView(ListView):
    model = Product
    extra_context = {'list_name': 'Продукты'}



class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

class ContactView(View):
    template_name = 'catalog/contacts.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"{name} ({email}): {message}")

        new_contact = create_contact_dict(name, email, message)

        contacts_base = read_JSON_data(contacts_base_file)

        contacts_base.append(new_contact)

        write_JSON_data(contacts_base_file, contacts_base)

        return render(request, self.template_name)
