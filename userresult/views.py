from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from mlab.models import USER_RESULT,Tests,bloodsugar,userprofile,cholesterol,urinalysis
from django.views import generic
from django.views.generic import View
from django.urls import reverse_lazy
from .utils import render_to_pdf
from django.template.loader import get_template
import os
from datetime import date
from django.conf import settings
from django.http import HttpResponse, Http404

# Create your views here.
# class GeneratePdf(View):
#     def get(self, request, *args, **kwargs):
#         data = {
#              'today': datetime.date.today(), 
#              'amount': 39.99,
#             'customer_name': 'Cooper Mann',
#             'order_id': 1233434,
#         }
#         pdf = render_to_pdf('testresults/bloodsugar.html', data)
#         return HttpResponse(pdf, content_type='application/pdf')

def bloodsugarview(request, tstrs_id, *args, **kwargs):
    id = request.user
    usr = userprofile.objects.get(user_id=id)
    tstrs = bloodsugar.objects.get(id=tstrs_id)
    born = usr.dob
    today = date.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    data = {
        'name': request.user.first_name,
        'age': age, 
        'gender': usr.gender,
        'date': tstrs.testdate,
        'val': tstrs.observedval,
    }
    pdf = render_to_pdf('testresults/bloodsugar.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

def cholesterolview(request, tstrs_id, *args, **kwargs):
    id = request.user
    usr = userprofile.objects.get(user_id=id)
    tstrs = cholesterol.objects.get(id=tstrs_id)
    born = usr.dob
    today = date.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    data = {
        'name': request.user.first_name,
        'age': age, 
        'gender': usr.gender,
        'date': tstrs.testdate,
        'tc': tstrs.totalcholesterol,
        'ldl': tstrs.ldl,
        'hdl': tstrs.hdl,
        'triglycerides': tstrs.triglycerides,
    }
    pdf = render_to_pdf('testresults/cholesterol.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

def urinalysisview(request, tstrs_id, *args, **kwargs):
    id = request.user
    usr = userprofile.objects.get(user_id=id)
    tstrs = urinalysis.objects.get(id=tstrs_id)
    born = usr.dob
    today = date.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    data = {
        'name': request.user.first_name,
        'age': age, 
        'gender': usr.gender,
        'date': tstrs.testdate,
        'color': tstrs.color,
        'turpidity': tstrs.turpidity ,
        'ph': tstrs.ph,
        'glucose': tstrs.glucose,
        'bilirubin': tstrs.bilirubin,
        'blood': tstrs.blood,
        'protien': tstrs.protien,
        'leukocyte': tstrs.leukocyte 
    }
    pdf = render_to_pdf('testresults/urinalysis.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

def history(request):
    
    id = request.user
    if bloodsugar.objects.filter(userid_id=id).exists() or cholesterol.objects.filter(userid_id=id).exists() or urinalysis.objects.filter(userid_id=id).exists():
        if bloodsugar.objects.filter(userid_id=id).exists() and cholesterol.objects.filter(userid_id=id).exists() and urinalysis.objects.filter(userid_id=id).exists():
            bres = bloodsugar.objects.filter(userid_id=id)
            cres = cholesterol.objects.filter(userid_id=id)
            ures = urinalysis.objects.filter(userid_id=id)
            context1 = {
            'cres': cres,
            'bres': bres,
            'ures': ures
            }
        elif bloodsugar.objects.filter(userid_id=id).exists() and cholesterol.objects.filter(userid_id=id).exists():
            print("cholesterol object is present")
            cres = cholesterol.objects.filter(userid_id=id)
            bres = bloodsugar.objects.filter(userid_id=id)
            context1 = {
            'cres': cres,
            'bres': bres
            }
        elif cholesterol.objects.filter(userid_id=id).exists() and urinalysis.objects.filter(userid_id=id).exists():
            cres = cholesterol.objects.filter(userid_id=id)
            ures = urinalysis.objects.filter(userid_id=id)
            context1 = {
            'cres': cres,
            'ures': ures
            }
        elif bloodsugar.objects.filter(userid_id=id).exists() and urinalysis.objects.filter(userid_id=id).exists():
            bres = bloodsugar.objects.filter(userid_id=id)
            ures = urinalysis.objects.filter(userid_id=id)
            context1 = {
            'bres': bres,
            'ures': ures
            }
        elif urinalysis.objects.filter(userid_id=id).exists():
            ures = urinalysis.objects.filter(userid_id=id)
            context1 = {
            'ures': ures
            }
        elif cholesterol.objects.filter(userid_id=id).exists():
            cres = cholesterol.objects.filter(userid_id=id)
            context1 = {
            'cres': cres
            }
        else:
            bres = bloodsugar.objects.filter(userid_id=id)
            context1 = {
            'bres': bres
            }
          
        return render(request,'userresult.html',context1)
    else:
        return render(request,'index.html')
  
def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exits(file_path):
        with open(file_path,'rb')as fh:
            response=HttpResponse(fh.read(), content_type="application/testresult")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response

    raise Http404
  
