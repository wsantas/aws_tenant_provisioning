from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, 'home.html')


def new_tenant_page(request):
    return render(request, 'new-tenant.html', {
        'new_item_text': request.POST.get('client_id', ''),
    })
