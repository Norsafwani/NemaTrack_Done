from django.urls import path, include, re_path
from django.views.generic import TemplateView
from trackApp import views
from trackApp.controller import usercontroller, nemacontroller,nemareturncontroller 

urlpatterns = [

    #First Page = Login Page
    # path("",views.indexhome, name="indexhome"),567
    # path('',views.indexhome),

    path('', views.index),
    path('home', usercontroller.home, name="home"),
    # path('home', nemacontroller.endclientlist),

    #INDEX- Display Nema Data
    path ('indexnema',nemacontroller.indexnema, name='indexnema'),

    #INDEX- Display End Client Data at Home
    # path ('clientnema',nemacontroller.clientnema, name='clientnema'),

    #ADD NEW NEMA
    path ('nemacreate', nemacontroller.nemacreate),
    path ('nemaexcel', nemacontroller.nemaexcel),

    #SUBMIT ADD NEW
    path('submitnema',nemacontroller.submitnema),

    #DELETE 
    path ('deletenema/<int:nema_id>', nemacontroller.deletenema),

    #UPDATE
    path('updatenema/<int:nema_id>',nemacontroller.updatenema),

    #UPDATE SUBMIT
    path('updatesubmitnema',nemacontroller.updatesubmitnema),

    #SEARCH 
    path('searchnema',nemacontroller.searchnema),

    #LOGIN
    path('submit_login', usercontroller.submit_login),

    #LOGOUT
    path('logout_nema',usercontroller.logout_nema),

    #VIEW
    path('viewnema/<int:nema_id>',nemacontroller.viewnema),
    
    #RETURN FORM NEMA
    path('returnformnema/<int:nema_id>',nemareturncontroller.returnformnema),

    #UPLOAD EXCEL FILE
    path ('get_excel',nemacontroller.get_excel, name='get_excel'),

    # path ('save_file_second',nemacontroller.save_file_second, name='save_file_second'),

    #Try - Display DATA Excel table
    path ('indexexcelnema',nemacontroller.indexexcelnema, name='indexexcelnema'),

    #DELETE RETURN FORM LIST
    path ('deletenemareturn/<int:return_id>', nemareturncontroller.deletenemareturn),

    #UPDATE RETURN FORM LIST
    path('updatenemareturn/<int:return_id>',nemareturncontroller.updatenemareturn),

    #UPDATE SUBMIT RETURN FORM
    path('updatesubmitnemareturn',nemareturncontroller.updatesubmitnemareturn),

    #SUBMIT ADD TRY NEMA2
    path('submitreturnform',nemareturncontroller.submitreturnform),

    #RETURN FORM LIST
    path ('return_nema',nemareturncontroller.return_nema, name='return_nema'),

    #SUBMIT RETURN FORM
    path ('save_file_second',nemacontroller.save_file_second, name='save_file_second'),

]
