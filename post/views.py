from django.shortcuts import render,redirect
from . models import Patient, Emergency
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage


# Create your views here.

def patient(request):
    patients  = Patient.objects.all().values()
    return  render(request, 'card/data_details.html', {'patients':patients})

def create_patient(request):

    if request.method == 'POST':
        if request.FILES['photo']:
            upload_photo = request.FILES['photo']
            storage = FileSystemStorage()
            file = storage.save(upload_photo.name, upload_photo)
            photourl = storage.url(file)
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        gender = request.POST['gender']
        marital_status = request.POST['marital_status']
        nationality = request.POST['nationality']
        home_address = request.POST['home_address']
        home_phone_number = request.POST['home_phone_number']
        office_phone_number = request.POST['office_phone_number']
        age = request.POST['age']
        nin = request.POST['nin']
        office_address = request.POST['office_address']
        date_of_birth = request.POST['date_of_birth']

        patient = Patient(first_name=first_name,        middle_name=middle_name,
                    last_name=last_name, gender=gender,home_phone_number=home_phone_number,office_phone_number=office_phone_number,
                     nationality=nationality,   marital_status=marital_status,home_address=home_address,  age=age,nin=nin,office_address=office_address, date_of_birth=date_of_birth, photo=photourl )
        patient.save()
        return redirect('emergency')
    return render(request, 'card/create.html')

# def retrieve_all(request):

def edits(request, id):
    edit_data = Patient.objects.get(pk=id)

    if request.method == 'POST':
        edit_data.first_name = request.POST['first_name']
        edit_data.middle_name = request.POST['middle_name']
        edit_data.last_name = request.POST['last_name']
        edit_data.gender = request.POST['gender']
        edit_data.home_phone_number = request.POST['home_phone_number']
        edit_data.office_phone_number = request.POST['office_phone_number']
        edit_data.nationality = request.POST['nationality']
        edit_data.marital_status = request.POSt['marital_status']
        edit_data.home_address = request.POST['home_address']   
        edit_data.age = request.POST['age']
        edit_data.nin = request.POST['nin']
        edit_data.office_address = request.POST['office_address']
        edit_data.date_of_birth = request.POST['date_of_birth']
        edit_data.save()
        return redirect('patient')
    
    return render(request, 'card/edit.html', {'edit_data':edit_data})

def details(request, id):
    detail = Patient.objects.get(pk=id)
    patients = Patient.objects.all().values()
    context = {
        'detail': detail,
        'patients': patients
    }
    return render(request, 'card/pdetails.html',context)
    

def delete(request, id):
    delete_data = Patient.objects.get(pk=id)
    delete_data.delete()
    return redirect('patient')
# ///////////////////////////////////////////
def emergencys(request):
    emergencyss = Emergency.objects.all().values()
    return render(request, 'emergency/retrieve-all.html', {'emergencyss':emergencyss})


def emergency(request):
    if request.method == 'POST':
        if request.FILES['photo']:
            upload_photo = request.FILES['photo']
            storage = FileSystemStorage()
            file = storage.save(upload_photo.name, upload_photo)
            photourl = storage.url(file)
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        gender = request.POST['gender']
        home_address = request.POST['home_address']
        home_phone_number = request.POST['home_phone_number']
        relationship = request.POST['relationship']

        emergencys = Emergency(first_name=first_name, middle_name=middle_name, last_name=last_name, gender=gender, home_address=home_address,home_phone_number=home_phone_number, relationship=relationship,photo=photourl)
        emergencys.save()
        return redirect('patient')
    return render(request, 'emergency/emergency.html')
        