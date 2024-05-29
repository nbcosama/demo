from ast import Index
import json
from multiprocessing import context
from re import A
from tokenize import Number
from django.urls import reverse
from email import message
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index2(request):
    customer = Customers.objects.all()
    count = Class.objects.count()
    context = {
        'customer' : customer,
        'count' : count,   
    }
    return render(request, 'index2.html',context)

def viewdata(request, id):
    customer = Customers.objects.get(id=id)
    context = {
            'customer' : customer,
        }
    return render(request, 'bills.html',context )


def deletedata(request, id):
    member = Customers.objects.get(id=id)
    member.delete()
    messages.success(request, "Successfully added")
    return HttpResponseRedirect(reverse('index2'))

def bills2(request):
    if request.method =="POST":
        stname=request.POST.get('stname')
        classname=request.POST.get('classname')
        installmentname=request.POST.get('installmentname')
        feeamount=request.POST.get('feeamount')
        paidfee=request.POST.get('paidfee')
        disamount=request.POST.get('disamount')
        remainingamount=int(feeamount)-int(paidfee)
        
        data=Payments(student_name=stname,class_name=classname,Installment_name=installmentname,fee_amount=feeamount,paid_fee=paidfee,disc_amount=disamount, remainng_amount=remainingamount)
        data.save()
        messages.success(request, "Successfully added")
    bill = Addbills.objects.get(id=request.GET['bill_id'])
    grade = bill.Class
    member = Customers.objects.filter(Class_name = grade).all()
    data = []
    for i in member:
        userData = {
            'name': i.student_name,
            'total_amount': bill.Installment_amount,
            'bill_name': bill.Installment_name,
            'class': grade,
        }
        data.append(userData)
    return render(request, 'bills2.html', {"data": data})



def update(request, id):
    customers = Customers.objects.get(id=id)
    context = {
    'customers': customers,
     }
    return render(request, 'adduser.html',context )

def updaterecord(request, id):
    first = request.POST.get('fnumber')
    last = request.POST.get('Dnumber')
    member = Customers.objects.get(id=id)
    # member2 =Classes.objects.get(id=member.Class_name.id).total_amt
    member2 =member.final_amt
    member5 =member.paid_amt
  
    member4 =int(first)+int(member5)
    member.paid_amt = member4
    member3 =int(member2)-int(member.paid_amt)
    member.remaining_fee =member3
    
    member.save()
    return redirect('/' )


def uploapayment(request):
    if request.method =="POST":
        stname=request.POST.get('stname')
        classname=request.POST.get('classname')
        installmentname=request.POST.get('installmentname')
        feeamount=request.POST.get('feeamount')
        paidfee=request.POST.get('paidfee')
        disamount=request.POST.get('disamount')
        remainingamount=int(feeamount)-int(paidfee)
        
        data=Payments(student_name=stname,class_name=classname,Installment_name=installmentname,fee_amount=feeamount,paid_fee=paidfee,disc_amount=disamount, remainng_amount=remainingamount)
        data.save()
        messages.success(request, "Successfully added")
        return redirect("/contact")
    else:    
      return redirect(request, '/')     










def index(request):
    
    if request.method =="POST":
        firstname=request.POST.get('fname')
        lstname=request.POST.get('snumber')
        location=request.POST.get('tnumer')
        fnumber=int(request.POST.get('fnumber'))
        Dnumber=int(request.POST.get('Dnumber'))
        multiply = fnumber*Dnumber
        # percent =  fnumber*Dnumber/100
       
        data=Class(num_name=firstname,class_name=lstname,section_nmae=location,monthly_fee=fnumber,Fee_for_month=Dnumber,total_fee=multiply,)
        data.save()
        messages.success(request, "Successfully added")
        return redirect("index")
    else:
        clss = Class.objects.all()
        count = Class.objects.count()
        context = {
            'clss' : clss,
            'count' : count
        }   
        return render(request, 'index.html',context)

       

def about(request):
    djtext = request.GET.get('text','defult')
    analyze = djtext
    if len(djtext)<5:
        prams = {'disc':'Tu bahut Alsi Haire baba tere se nahi hoga tu nikal'}
        return render(request,'about.html',prams)
    else:
        param = {'name':'osama', 'count':len(djtext), 'Countary':analyze}
        return render(request,'about.html' , param)
    
    
def contact(request):
    person = Person2.objects.all()
    counts = Person2.objects.count()
    total= []
    daes = Class.objects.all()
    for i in daes:
        total.append( counts* int(i.total_fee))
    context = {
        'person' : person,
        'counts' : counts,
        'total' : total
    }
    return render(request, 'contact.html',context )      



def uploadata(request):
    dpname=Department.objects.all()
    
    if request.method =="POST":
        firstname=request.POST.get('first_name')
        lstname=request.POST.get('last_name')
        location=request.POST.get('location')
        print(firstname)
        
        data=Person2(first_name2=firstname,last_name=lstname,depr_name_id=location)
        data.save()
        
        return redirect("uploadata", )
    else:    
      msg= messages.success(request, "Successfully added")
      context={'dpname':dpname,'msg':msg}
      return render(request, 'uploadata.html',context)       
  
  
def delete(request, id):
    member = Class.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def profile(request, id):
    clss = Class.objects.get(id=id)
    context = {
            'clss' : clss,
        }
    return render(request, 'profile.html',context )      


def customers(request):
    return render(request, 'customers.html')


def bills(request):
    return render(request, 'bills.html')

def reports(request):
    return render(request, 'reports.html')

def adduser(request):
    return render(request, 'adduser.html')



def upload_image(request):
    if request.method == 'POST':
        image = request.FILES['image']
        selected_students = request.POST.getlist('selected_students')
        inner_list_string = selected_students[0]
        inner_list = json.loads(inner_list_string)
        first_value = inner_list[0]
        print(first_value)
        UploadedImage.objects.create(image=image, student_id=first_value)
        print(selected_students)
        print('osama')
        messages.success(request, "Successfully Uploaded")
        return redirect('upload_image')
    allimages = UploadedImage.objects.all()
    allstudent = Student.objects.all()
    context= {'allimages':allimages, 'allstudent':allstudent}
    return render(request, 'uploadimage.html',context)