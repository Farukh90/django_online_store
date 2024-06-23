from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from catalog.utils import read_JSON_data
from catalog.utils import write_JSON_data
from catalog.utils import create_contact_dict
from catalog.models import Category, Product

contacts_base_file = r'contacts.json'


# Create your views here.
def products_list(request):
    products = Product.objects.all()
    context = {"product_list": products}
    return render(request, 'catalog/product_list.html', context)


class ProductListView(ListView):
    model = Product
    extra_context = {'list_name': 'Продукты'}


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'catalog/product_detail.html',context)



def contacts(request):
    '''обрабатывает POST запрос и сохраняет контактные данные в файл JSON'''
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"{name} ({email}): {message}")

        new_contact = create_contact_dict(name, email, message)

        contacts_base = read_JSON_data(contacts_base_file)

        contacts_base.append(new_contact)

        write_JSON_data(contacts_base_file, contacts_base)


    return render(request, 'catalog/contacts.html')
