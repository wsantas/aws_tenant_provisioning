from django.conf.urls import url
from project.tenant_provisioning import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
]