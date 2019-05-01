from django.http import HttpResponse
from django.shortcuts import render
import boto3


# Create your views here.
def home_page(request):
    return render(request, 'home.html')


def new_tenant_page(request):
    return render(request, 'new-tenant.html')

def post_tenant(request):
    s3 = boto3.resource('s3')
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('tenant_id', ''),
    })

