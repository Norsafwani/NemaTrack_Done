# Create your views here. where all the functions lies
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from datetime import date, datetime
from trackApp.models import AuthUser, AuthPermission
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import logout, authenticate, login
from django.core.files.storage import FileSystemStorage
from trackApp.models import Nema, Returnformnema, Nemaexcel, Uploadnema
from django.contrib import messages

#Function 'Return Form Nema'
def returnformnema(request, nema_id):
    # admin = ''
    objNema = Nema.objects.get(nema_id=nema_id)
    obj = {
        'objNema': objNema
         }
    return render(request, 'nema/nema_form.html', obj)

#Function for Display Return Nema [List]
def return_nema(request):
    returnnema = Returnformnema.objects.all()
    # print('print this', product)
    content = {
        'returnnema':returnnema,
    }
    return render(request, 'nema/return_form_list.html', content)


#Function for Delete Nema Return Form
def deletenemareturn(request, return_id):
    deleteR = Returnformnema.objects.get(return_id=return_id)
    deleteR.delete()
    return redirect('/return_nema')

#Function for Update Nema Return Form
def updatenemareturn(request,return_id):
    nemaR = Returnformnema.objects.get(return_id=return_id)
    obj = {
        'nemaR': nemaR,
    }
    return render(request, 'nema/return_update.html', obj)

#Function for Submit Update Nema Return Form
def updatesubmitnemareturn(request):

    if request.method == "POST":
        # Get the posted form     
        return_id = request.POST['return_id']  
        dateuninstall = request.POST['dateuninstall']       
        datedetect = request.POST['datedetect']       
        proof_describe = request.POST['proof_describe']
        no_siri = request.POST['no_siri']
   
        nemaR = Returnformnema.objects.get(return_id = return_id )
        nemaR.dateuninstall = dateuninstall
        nemaR.datedetect = datedetect
        nemaR.proof_describe = proof_describe
        nemaR.no_siri = no_siri
        nemaR.save()

    return redirect('/return_nema')

#Funtion for submit Return Form Nema
def submitreturnform(request):
    
    # if request.method=='POST':

        # devui_id = request.POST['devui']
        # print(devui_id)

        date_uninstall = request.POST['dateuninstall']
        print(date_uninstall)

        date_detect = request.POST['datedetect']   
        print(date_detect)

        proofdescribe = request.POST['proof_describe']          
        nosiri = request.POST['no_siri']

        image_proof = request.FILES.get('report_img','')
        nema = request.POST['nema_id']
        
        try:
            filename = None
            if image_proof != '':
                the_file = request.FILES['report_img']
                fs = FileSystemStorage()
                path = 'trackNema/static/img/report/'
                filename = fs.save(path+'-'+the_file.name, the_file)
                uploaded_file_url = fs.url(filename)

            # masuk ke database
            formfile = Returnformnema(dateuninstall=date_uninstall,datedetect=date_detect, proof_describe=proofdescribe,
                                  no_siri=nosiri, nema_id=nema, image_proof=filename)
            formfile.save()
            return redirect('/return_nema')

        except Exception as e:
                return HttpResponse(e)
                print('Error',e)
                return redirect('/return_nema')




