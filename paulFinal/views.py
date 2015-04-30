from __future__ import division # to yeild the decimal point values in Python 2.x
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import auth
from django.core.context_processors import csrf
from paulApp.forms import OrderForm, DriverForm
from paulApp.models import OrderModel, DriverModel
from django.utils import timezone
from django.template import *
from datetime import datetime
from dateutil.parser import parse # to parse the unicode date


@login_required
def index(request):
	return render_to_response('index.html',{'name':request.user.username, 'data':OrderModel.objects.order_by('id').reverse()[:10] , 'driver':DriverModel.objects.order_by('reputation').reverse()[:10]},
                             context_instance=RequestContext(request))


@login_required
def all_records(request):
	return render_to_response('index.html',{'name':request.user.username, 'data':OrderModel.objects.order_by('id').reverse() , 'driver':DriverModel.objects.order_by('reputation').reverse()},context_instance=RequestContext(request))


def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login.html',c)

def validate(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user= auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else :
        return HttpResponseRedirect('/accounts/invalid/')
    
@login_required   
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/accounts/login/')

def status(request, status):
    dis_items=OrderModel.objects.filter(status=status)
    return render_to_response('filter.html',{'data':dis_items, 'status':status,'name':request.user.username})

def get_load(request,load):
    c={}
    c.update(csrf(request))
    load_data=OrderModel.objects.get(id=load)
    c['data']=load_data
    c['name']=request.user.username
    return render_to_response('load.html',c)

@login_required
def add_load(request):
    if request.POST:
        form= OrderForm(request.POST)
        if form.is_valid():
            del_date=request.POST.get('del_date')
            del_date=parse(del_date)
            if datetime.now()>= del_date:
                args={}
                args.update(csrf(request))
                args['form']=form
                args['errors']="Delivery Date is not Valid! Enter Valid Delivery Date"
                args['name']=request.user.username
                return render_to_response('forms.html',args,context_instance=RequestContext(request))
            else:
                form.save()
                name=request.POST.get('driver_name')
                b=DriverModel.objects.get(dl_no=name)
                task=b.assigned_tasks
                task+=1
                b.assigned_tasks=task
                b.reputation=reputation(b.finished_tasks,b.assigned_tasks)
                b.save()
                return HttpResponseRedirect('/')                    
    else:
        form=OrderForm()
    args={}
    args.update(csrf(request))
    args['form']=form
    args['name']=request.user.username
    return render_to_response('forms.html',args,context_instance=RequestContext(request))
  
@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_driver(request):
    if request.POST:
        form= DriverForm(request.POST)
        if form.is_valid():
            assigned_task=request.POST.get('assigned_tasks')
            finished_task=request.POST.get('finished_tasks')
            if assigned_task<finished_task:
                args={}
                args.update(csrf(request))
                args['form']=form
                args['name']=request.user.username
                args['errors']="Assigned tasks can't be smaller than Complete tasks!"
                return render_to_response('drivers.html',args)
            form.save()
            return HttpResponseRedirect('/#profile')
    else:
        form=DriverForm()
    args={}
    args.update(csrf(request))
    args['form']=form
    args['name']=request.user.username
    return render_to_response('drivers.html',args)

@login_required
def update_status(request, id):
    a=OrderModel.objects.get(id=id)
    if request.POST:
        status=request.POST.get('update_status')
        a.status=status
        dl=a.driver_name.dl_no
        if 'Complete' in a.status:
            d=DriverModel.objects.get(dl_no=dl)
            if d is not None:
                x=d.finished_tasks
                x+=1
                d.finished_tasks=x
                d.reputation=reputation(d.finished_tasks, d.assigned_tasks)
                d.save()
        a.save()
        return HttpResponseRedirect('/load_get/'+id+'/')
    else:
        return HttpResponseRedirect('/load_get/'+id+'/')
    
# This function calculates the reputation of the drivers  
def reputation(complete, assigned):
    rep=float((complete/assigned)*5)
    rep=round(rep)
    if rep==0:
        return 1
    else :
        return rep
    