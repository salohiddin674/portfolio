from django.shortcuts import render,redirect
from .models import *

def index_view(request):
    contex = {
        'banner': Banner.objects.last(),
        'resume':Resume.objects.last(),
        'bio': Bio.objects.last(),
        'info':Info.objects.all().order_by('-id')[:3],
        'people_say':People_saya.objects.all().order_by('-id')[:4],
        'faq':FAQ.objects.all().order_by('-id')[:5],
        'info1':Info1.objects.last(),

    }

    return render(request,'index.html',contex)

def contact_view(request):
    if request.method == 'POST':
        full_name=request.POST['full_name']
        email=request.POST['email']
        message=request.POST['message']
        Contact.objects.create(
            full_name=full_name,
            email=email,
            message=message,
        )
        return redirect('index_url')


