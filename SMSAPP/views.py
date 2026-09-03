from django.shortcuts import render,redirect
from.models import sms
import json
from django.http import HttpResponse


def Mainpage(request):
    if request.method=='GET':
        data=sms.objects.all()
        return render (request,'mainpage.html',{'data':data})

def add_student(request):
    if request.method=='GET':
        data=sms.objects.all()
        return render (request,'add_student.html',{'data':data})
    else:
        fname1=request.POST.get('fname')
        lname1=request.POST.get('lname')
        email1=request.POST.get('email')
        mobile1=request.POST.get('mobile')
        percentage1=request.POST.get('percentage')
        year1=request.POST.get('year')
        location1=request.POST.get('location')
        college1=request.POST.get('college')
        university1=request.POST.get('university')
        sms(
        first_name=fname1,
        last_name=lname1,
        email=email1,
        mobile=mobile1,
        percentage=percentage1,
        year=year1,
        location=location1,
        college=college1,
        universsity=university1,
        ).save()
        data=sms.objects.all()
        return render(request,'add_student.html',{'data':data})

def view_student(request):
    if request.method=='GET':
        data=sms.objects.all()
        return render (request,'view_student.html',{'data':data})

def search_student(request):
    if request.method=='POST':
        name=request.POST.get('fname', '').strip()
        data=sms.objects.filter(first_name__icontains=name)
        return render(request,'search.html',{'data':data})
    else:
        return render(request,'search.html')

def update(request,id):
    data=sms.objects.get(id=id)
    return render (request,'update.html',{"data":data})

def update_data(request,id):
    data=sms.objects.get(id=id)
    if request.method=='POST':
        data.first_name=request.POST.get('fname')
        data.last_name=request.POST.get('lname')
        data.email=request.POST.get('email')
        data.mobile=request.POST.get('mobile')
        data.percentage=request.POST.get('percentage')
        data.year=request.POST.get('year')
        data.location=request.POST.get('location')
        data.college=request.POST.get('college')
        data.universsity=request.POST.get('university')
        data.save()
        return redirect('Mainpage')

def delete_student(name,id):
    data=sms.objects.get(id=id)
    data.delete()
    return redirect('Mainpage')

def save_file(request):

    students = sms.objects.all()

    data = []

    for student in students:
        data.append({
            'first_name': student.first_name,
            'last_name': student.last_name,
            'email': student.email,
            'mobile': student.mobile,
            'percentage': student.percentage,
            'year': student.year,
            'location': student.location,
            'college': student.college,
            'university': student.universsity
        })

    with open('students.json', 'w') as file:
        json.dump(data, file, indent=4)

    return HttpResponse("Data saved successfully")

def load_file(request):

    with open('students.json', 'r') as file:
        data = json.load(file)

    for student in data:

        sms.objects.get_or_create(
            first_name=student['first_name'],
            last_name=student['last_name'],
            email=student['email'],
            mobile=student['mobile'],
            percentage=student['percentage'],
            year=student['year'],
            location=student['location'],
            college=student['college'],
            universsity=student['university']
        )

    return redirect('Mainpage')
