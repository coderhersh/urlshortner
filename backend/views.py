from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Url
from .get_short_ulr import return_short_url
from .verify_long_url import isvalid_long_url
from datetime import datetime

# / must be there in the end of every URL

def index(request):
    return render(request, 'form.html')

def short_url_to_long_url(request, requested_short_url):
    if Url.objects.filter(short_url=requested_short_url).exists():
        obj = Url.objects.get(short_url = requested_short_url)
        obj.count += 1
        obj.save()
        return redirect(f'{obj.long_url}')
    else:
        messages.info('Url you entered has either expired or does not exist')

def submit(request):
    if request.method == 'POST':
        long_url = request.POST['longurl']
        if(isvalid_long_url(long_url) == False):
            return HttpResponse('You have entered an invalid url')

        if(Url.objects.filter(long_url=long_url).exists()):
            obj = Url.objects.get(long_url=long_url)
            return render(request, 'result.html', {'url':obj})

        temp_short_url = return_short_url()
        
        while True:
           if Url.objects.filter(short_url=temp_short_url).exists() == False:
                break
           else:
            temp_short_url = return_short_url()

        obj = Url(long_url=long_url, short_url=temp_short_url, created_on=datetime.now())
        obj.save()
    
    return render(request, 'result.html', {'url':obj})
