from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^showLogin/$',views.showLogin,name  = 'showLogin'),
]


