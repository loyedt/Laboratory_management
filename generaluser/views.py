from django.shortcuts import render, redirect
from django.contrib import messages
from mlab.models import general_user

import os
from django.conf import settings
from django.http import HttpResponse, Http404
# Create your views here.
def result(request):
    if request.method == 'POST':
        tstno = request.POST['tstno']
        phno  = request.POST['phno']
        if general_user.objects.filter(tstno=tstno).exists():
            if general_user.objects.filter(phno=phno).exists():
                res = general_user.objects.get(tstno=tstno,phno=phno)
                return render(request,"specificresult.html",{'res':res})
                # res = general_user.objects.get(tstno=tstno,phno=phno)
                # rspath = res.tstrst
                # download(request,{res.tstrst.url})
            else:
                messages.info(request,' Invalid inputs')
                return redirect('result')
        else:
            messages.info(request,' Invalid inputs')
            return redirect('result')
    else:
        return render(request,"generalresult.html")

def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exits(file_path):
        with open(file_path,'rb')as fh:
            response=HttpResponse(fh.read(), content_type="application/testresult")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response

    raise Http404
    