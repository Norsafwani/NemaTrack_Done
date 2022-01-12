# Create your views here. where all the functions lies
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from datetime import date, datetime
from trackApp.models import AuthUser, AuthPermission
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import logout, authenticate, login
from django.core.files.storage import FileSystemStorage
from trackApp.models import Nema, Returnformnema, Nemaexcel, Uploadnema,Nemaexcel
import openpyxl #For Upload Excel
from django.contrib import messages

#Function for Display Nema Data
def indexnema(request):
    nema = Nema.objects.all()
    # print('print this', product)
    content = {
        'nema':nema,
    }
    return render(request, 'nema/nema_data.html', content)


#TRY Function for Display Nema Excel Data
def indexexcelnema(request):
    nemaEx = Nema.objects.all()
    # print('print this', product)
    content = {
        'nemaEx':nemaEx,
    }
    return render(request, 'nema/try_data_excel.html', content)

#Function for html create new Nema
def nemacreate(request):
    return render(request,'nema/nema_create.html',{})

#Function Submit Create New Nema
def submitnema(request):
    # id = request.session['id']
    # if request.session._session:
        if request.method=='POST':
            # nema_id = request.POST['id']
            devui_no = request.POST['devui']
            appkey = request.POST['app_key']
            shipdatereceived = request.POST['ship_date_received']
            siteinstalldate = request.POST['site_install_date']
            datedeliver = request.POST['date_deliver']           
            lightsolname = request.POST['lightsol_name']           
            licenseactivedate = request.POST['license_active_date']          
            licenseexpireddate = request.POST['license_expired_date']          
            contractorname = request.POST['contractor_name']           
            endclientname = request.POST['end_client_name']           
            projecttendername = request.POST['project_tender_name']           
            donumber = request.POST['do_number']            
            remarks = request.POST['remarks']

            # For insert into database-id= nema_id,
            # object = nama model( namacolumn=nama variable, others - if any)
            track = Nema(devui=devui_no, app_key=appkey, ship_date_received=shipdatereceived, site_install_date= siteinstalldate, 
            date_deliver=datedeliver, lightsol_name = lightsolname, license_active_date=licenseactivedate, license_expired_date= licenseexpireddate,
            contractor_name= contractorname,  end_client_name= endclientname, project_tender_name= projecttendername, 
            do_number= donumber, remarks= remarks )
            track.save()
            return redirect('/indexnema')


#Function for Delete Nema Data
def deletenema(request, nema_id):
    deleteN = Nema.objects.get(nema_id=nema_id)
    deleteN.delete()
    # success_url = reverse_lazy('indexproduct')
    return redirect('/indexnema')

#FUNCTION FOR Update Nema Data
def updatenema(request,nema_id):
    nema = Nema.objects.get(nema_id=nema_id)
    obj = {
        'nema': nema,
    }
    return render(request, 'nema/nema_update.html', obj)

#FUNCTION FOR Submit Update Nema Data
def updatesubmitnema(request):
    if request.method == "POST":
        # Get the posted form     
        nema_id = request.POST['nema_id']  
        devui_no = request.POST['devui']       
        appkey = request.POST['app_key']       
        shipdatereceived = request.POST['ship_date_received']
        siteinstalldate = request.POST['site_install_date']
        datedeliver = request.POST['date_deliver']         
        lightsolname = request.POST['lightsol_name']      
        licenseactivedate = request.POST['license_active_date']      
        licenseexpireddate = request.POST['license_expired_date']       
        contractorname = request.POST['contractor_name']      
        endclientname = request.POST['end_client_name']   
        projecttendername = request.POST['project_tender_name']     
        donumber = request.POST['do_number']    
        remarks = request.POST['remarks']
        #product_file
    
        nema = Nema.objects.get(nema_id =nema_id )
        nema.devui = devui_no
        nema.app_key = appkey
        nema.ship_date_received = shipdatereceived
        nema.site_install_date = siteinstalldate
        nema.date_deliver = datedeliver
        nema.lightsol_name = lightsolname
        nema.license_active_date = licenseactivedate
        nema.license_expired_date = licenseexpireddate
        nema.contractor_name = contractorname
        nema.end_client_name = endclientname
        nema.project_tender_name = projecttendername
        nema.do_number = donumber
        nema.remarks = remarks 

        nema.save()

    return redirect('/indexnema')
#END TRY

#Function for Searching 
def searchnema(request):
    # global nemas
    if request.method == "POST":
        searchNema =  request.POST['searchNema'] 
        #nemas(Return search result)
        nemas = Nema.objects.filter(devui__contains=searchNema)
        nemas2 = Nema.objects.filter(app_key__contains=searchNema)

        # app_key__contains=searchNema
        obj = {
        'searchNema': searchNema,
        'nemas': nemas,
        'nemas2': nemas2,
        }

        return render(request, 'nema/nema_search.html', obj)
    else:
        return render(request, 'nema/nema_search.html', {})


#UPLOAD EXCEL TO DATABASE - JADI!
def get_excel(request):
    import openpyxl
    adddevicetype = request.POST['adddevicetype2']
    # return HttpResponse(adddevicetype)
    # organizationid = request.session['organizationid']
    # userid = request.session['userid']

    excel_file = request.FILES["excel_file"]
    wb = openpyxl.load_workbook(excel_file)
    worksheet = wb["Sheet1"] 
    count = countsuccess = countfail = 0 
    msg = 'none'

    for row in worksheet.iter_rows(min_row=2,values_only=True):
        count = count + 1

        devuid = str(row[0])
        app_keyd = str(row[1])
        shipdatereceived = str(row[2])
        siteinstalldate = str(row[3])
        # datedeliver = row[4]
        lightsolname = str(row[5])
        # licenseactivedate = str(row[6])
        # licenseexpireddate = str(row[7])
        contractorname = str(row[8])
        # endclientname = str(row[9])
        # projecttendername = str(row[10])
        # donumber = str(row[11])
        # remarks = str(row[12])
        try:
            # Convert to Datetime object
            siteinstalldate = func.strdateToDate(siteinstalldate) 
            
            nema = Nemaexcel(devui_d=devuid, app_key_d= app_keyd,ship_date_received_d=shipdatereceived, 
                    site_install_date=siteinstalldate, lightsol_name=lightsolname, contractor_name= contractorname)
                    # end_client_name=endclientname,project_tender_name=projecttendername,
                    # do_number=donumber,remarks=remarks ) date_deliver=datedeliver,license_active_date=licenseactivedate, 
                    # license_expired_date=licenseexpireddate,
                    nema.save()

        except:
            siteinstalldate = now

        

    return redirect('/home')

#Function for Add Nema using Excel
def nemaexcel(request):
    return render(request,'nema/nema_excel.html',{})

#Try Upload File/images
def save_file_second(request):

    dateuninstall = request.POST['dateuninstall']
    datedetect = request.POST['datedetect']
    proofdescribe = request.POST['proof_describe']
    no_siri = request.POST['no_siri']
    # report = request.POST['name_file']
    nema = request.POST['nema_id']
    image_proof = request.FILES.get('sl_report_img','')
    pdf_proof = request.FILES.get('sl_report_img','')

    try:
        filename = None
        if image_proof != '':
            the_file = request.FILES['sl_report_img']
            fs = FileSystemStorage()
            path = 'trackApp/static/files'
            filename = fs.save(path+'-'+the_file.name, the_file)
            uploaded_file_url = fs.url(filename)

        savefile = Returnformnema(dateuninstall=dateuninstall,datedetect=datedetect, proof_describe=proofdescribe,
                no_siri=no_siri, nema_id=nema, image_proof=filename)
        savefile.save()
        return redirect('/home')
    
    except Exception as e:
            return HttpResponse(e)
            print('Error',e)
            return redirect('/return_nema')


#TRY Function for Display Nema Excel Data
def indexexcelnema(request):
    nemaEx = Nemaexcel.objects.all()
    # print('print this', product)
    content = {
        'nemaEx':nemaEx,
    }
    return render(request, 'nema/try_data_excel.html', content)

# 

#Function fo view 1 specific Nema
def viewnema(request,nema_id):
    # admin = ''
    objnema = Nema.objects.get(nema_id=nema_id)
    obj = {
        'objnema': objnema
    }
    return render(request, 'nema/nema_view.html', obj)

#Function for output the client list at home
# def endclientlist(request):
#     endclientlist = Nema.objects.all()
#     # print('print this', product)
#     content = {
#         'endclientlist':endclientlist,
#     }
#     return render(request, 'home.html', content)

#Function for Display Return Nema [List]
# def clientnema(request):
#     client = Nema.objects.all()
#     # print('print this', product)
#     content = {
#         'client':client,
#     }
#     return render(request, 'home.html', content)

#Function Date
# def strdatetimeToDatetime(strdate):
#     datetime2 = datetime.strptime(strdate, '%Y-%m-%d')
#     # return datetime2

#Function 'Return Form Nema'
# def returnformnema(request, nema_id):
#     # admin = ''
#     objNema = Nema.objects.get(nema_id=nema_id)
#     obj = {
#         'objNema': objNema
#          }
#     return render(request, 'nema/nema_form.html', obj)

#Function for Display Return Nema [List]
# def return_nema(request):
#     returnnema = Returnformnema.objects.all()
#     # print('print this', product)
#     content = {
#         'returnnema':returnnema,
#     }
#     return render(request, 'nema/return_form_list.html', content)

#Funtion for submit Return Form Nema
# def submitreturnform(request):
    
#     # if request.method=='POST':

#             # devui_id = request.POST['devui']
#             # print(devui_id)

#         date_uninstall = request.POST['dateuninstall']
#         print(date_uninstall)

#         date_detect = request.POST['datedetect']   
#         print(date_detect)

#         proofdescribe = request.POST['proof_describe']          
#         nosiri = request.POST['no_siri']

#         image_proof = request.FILES.get('report_img','')
#         nema = request.POST['nema_id']
        
#         try:
#             filename = None
#             if image_proof != '':
#                 the_file = request.FILES['report_img']
#                 fs = FileSystemStorage()
#                 path = 'trackNema/static/img/report/'
#                 filename = fs.save(path+'-'+the_file.name, the_file)
#                 uploaded_file_url = fs.url(filename)

#             # masuk ke database
#             formfile = Returnformnema(dateuninstall=date_uninstall,datedetect=date_detect, proof_describe=proofdescribe,
#                                   no_siri=nosiri, nema_id=nema, image_proof=filename)
#             formfile.save()
#             return redirect('/return_nema')

#         except Exception as e:
#                 return HttpResponse(e)
#                 print('Error',e)
#                 return redirect('/return_nema')


#Function for Delete Nema Return Form
# def deletenemareturn(request, nema_id):
#     deleteN = Nema.objects.get(nema_id=nema_id)
#     deleteN.delete()
#     # success_url = reverse_lazy('indexproduct')
#     return redirect('/indexnema')

#Function for Update Nema Return Form
# def updatenemareturn(request,nema_id):
#     nema = Nema.objects.get(nema_id=nema_id)
#     obj = {
#         'nema': nema,
#     }
#     return render(request, 'nema/nema_update.html', obj)


