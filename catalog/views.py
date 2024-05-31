from django.shortcuts import render
from .utils import read_JSON_data
from .utils import write_JSON_data
from .utils import create_contact_dict

contacts_base_file = r'contacts.json'


# Create your views here.
def home_page(request):
    return render(request, 'catalog/index.html')


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
