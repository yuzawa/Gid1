#from django.shortcuts import render

# Create your views here.

#from django.http import HttpResponse
#from django.template import loader
#from django.shortcuts import Http404,render
from django.shortcuts import get_object_or_404, render

from .models import Report

def index(request):
    latest_report_list = Report.objects.order_by('-pub_date')[:1]
    context = {
        'latest_report_list': latest_report_list,
    }
    return render(request, 'portals/index.html', context)

#    response = latest_report_list[0].attacker
#    return HttpResponse(response)

def detail(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    return render(request, 'portals/detail.html', {'report': report})
    

def reports(request, report_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % report_id)