from django.urls import path
from EvApp.views import HomePage, RegisterView,signinview,Add_department,depart,signout,Mission,AddComplaintview,OfficerHomeView,UserComplaintView,DetailAddReport,DetailViewReport
from EvApp.views import Officersigninview,OfficerList,CompliantEdit,Usercomplaintdelete,Complaintdetailview,AnyoaddComplaint,TermserviceView,FeedbackformView,FeedbackView,Department_DetailsView
from django.contrib import admin
urlpatterns = [

    path('',HomePage.as_view(),name="index"),
    path('register/',RegisterView.as_view(),name="user_register"),
    path('login/',signinview.as_view(),name="login"),
    path('add/',Add_department.as_view(),name="add_dep"),
    path('depart/',depart.as_view(),name="alldep"),
    path('logout/',signout.as_view(),name="logout"),
    path('miss/',Mission.as_view(),name="mission"),
    path('officersignin/',Officersigninview.as_view(),name="officer_login"),
    path('addcomplaint/',AddComplaintview.as_view(),name="complaint"),
    path('Offhome/',OfficerHomeView.as_view(),name="Offhome"),
    path('usercomplaintlist/',UserComplaintView.as_view(),name="usercomplaintlist"),
    path('officerlist/',OfficerList.as_view(),name="officerlist"),
    path('officerlist/complaintedit/<int:pk>',CompliantEdit.as_view(),name="complaintedit"),
    path('usercompdel/<int:pk>',Usercomplaintdelete.as_view(),name="compdel"),
    path('detailview/<int:pk>',Complaintdetailview.as_view(),name='detailview'),
    path('anyaddcomp/',AnyoaddComplaint.as_view(),name="anyo"),
    path('terms/',TermserviceView.as_view(),name="terms_service"),
    path('feedback/<int:pk>',FeedbackformView.as_view(),name="feedback"),
    path('feedbackview/<int:pk>',FeedbackView.as_view(),name="feedback_view"),
    path('anyaddcomp/',AnyoaddComplaint.as_view(),name="anyo"),
    path('Detailre/<int:pk>',DetailAddReport.as_view(),name='Dete'),
    path('Detailview/<int:pk>',DetailViewReport.as_view(),name='Deteview'),
    path('DepartmentDetails/<int:pk>',Department_DetailsView.as_view(),name="departmentdetails"),
  

    

]