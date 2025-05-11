from django.shortcuts import render
from django.http import HttpResponse
from base.models import *
# Create your views here.
def HomeView(request):
    items = Items.objects.all()
    list = Item_List.objects.all()
    review = Feedback.objects.all()
    return render(request,'index.html', {'items': items, 'list': list, 'review': review})

def AboutView(request):
    data = AboutUs.objects.all()
    return render(request, 'about.html', {'data': data})


def MenuView(request):
    items = Items.objects.all()
    list = Item_List.objects.all()
    return render(request,'menu.html', {'items': items, 'list': list})


def BookTableView(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Phone_Number = request.POST.get('Phone_Number')
        Email = request.POST.get('Email')
        total_person = request.POST.get('total_person')
        booking_date = request.POST.get('booking_date')
        if Name != '' and Email != '' and total_person != '' and booking_date != '' and len(Phone_Number) == 10 :
            data = Booktable(Name=Name, Phone_Number=Phone_Number,Email=Email,total_person=total_person,booking_date=booking_date)
            data.save()
    return render(request,'book.html')

def feedbackview(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Description = request.POST.get('Description')
        Rating = request.POST.get('Rating')
        Image = request.FILES.get('Image')
        if Name != '' and Description != '' and Rating != '' and Image is not None:
            data = Feedback(Name=Name,Description=Description,Rating=Rating,Image=Image)
            data.save()
    return render(request, 'feedback.html')