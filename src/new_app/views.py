from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LinkForm
from .models import Link
from django.conf import settings


host = settings.ALLOWED_HOSTS[-1]
# Create your views here.


def hello_world(request):
    form =  LinkForm()
    links = Link.objects.all()
    if request.method == 'POST':
        save_form = LinkForm(request.POST)
        save_form.save()
    return render(request, 'index.html', {'form':form,'links':links, 'host':host})

def get_link(request, link_code):
    link = Link.objects.get(new_link=link_code)
    return redirect(link.old_link)
