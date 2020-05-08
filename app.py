Open project in VSCODE
Go to terminal
cd jangos
workon test --#start env - test
python manage.py startapp calc --#it will create a app with name calc 

##we need to craet a separate url for our individual app as we have several
app in a single project so we need to maitain separate urls for separete apps.

urls.py\calc
from django.urls import path

from . import views
urlpatterns = [
    
    path('',views.home,name="home"),
    
]


urls.py\jangos

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('calc.urls')),
    path('admin/', admin.site.urls),
]

views.py:-

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('''<h1>"hello user"<h1>''')
