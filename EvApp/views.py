from django.shortcuts import render,redirect
from django.views.generic import View, CreateView,ListView
from django.contrib.auth import authenticate,login,logout
from EvApp.forms import Register,signin,Addform, OfficerSignin,Addcomplaint,AnyAddcomplaint,FeedbackForm,DetailForm
from django.urls import reverse_lazy
from EvApp.models import Department,CustUser,Complaint
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.conf import settings
# import certifi
# EMAIL_USE_SSL = True  # or EMAIL_USE_TLS = True
# EMAIL_SSL_CERTFILE = certifi.where()

# Create your views here.

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            return redirect("login")
    return wrapper

#@method_decorator(signin_required,name="dispatch")
class HomePage(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")

    
class RegisterView(CreateView):
    template_name = "register.html"
    form_class = Register
    model =CustUser
    success_url = reverse_lazy("index")
            

class Officersigninview(View):
    def get(self,request,*args,**kwargs):
        form=OfficerSignin()
        return render(request,"officer_login.html",{"form":form})   

    def post(self,request,*args,**kwargs):
        form=OfficerSignin(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_obj=authenticate(request,username=u_name,password=pwd)
            if user_obj and user_obj.is_officer :
                login(request,user_obj)
                return redirect("Offhome")
            else:
                print("false credentials")
        return redirect("officer_login")     


class signinview(View):
    def get(self,request,*args,**kwargs):
        form=signin()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=signin(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_obj=authenticate(request,username=u_name,password=pwd)
            if user_obj and user_obj.is_officer==0:
                login(request,user_obj)
                return redirect("index")
            else:
                print("false credentials")
        return redirect("login")    
@method_decorator(signin_required,name="dispatch")   
class Add_department(View):
    def get(self,request,*args,**kwargs): 
        form=Addform()
        return render(request,"add_dept.html", {"form":form})
    
    def post(self,request,*args,**kwargs):
        form=Addform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
           
            return render(request, "add_dept.html", {"form": form})
        
@method_decorator(signin_required,name="dispatch")
class depart(ListView):
    model=Department
    template_name="depart.html"
    context_object_name="department"

class signout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("index")
    

class Mission(View):
    def get(self,request,*args,**kwargs):  
        return render (request,"mission.html")
    
class AddComplaintview(View):
    def get(self,request,*args,**kwargs):
        form=Addcomplaint()
        return render(request,"complaint.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=Addcomplaint(request.POST,files=request.FILES)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.username = request.user.username
            complaint.save()
            form=Addcomplaint()
            return redirect("index")
        else:
            return render(request, "add_dept.html", {"form": form})
        
class OfficerHomeView(View):
    def get(self,request,*args,**kwargs):
        department = request.user.departments
        data=Complaint.objects.filter(department=department).order_by('status')
        return render(request,"complaintview.html",{"data":data})
    
class UserComplaintView(View):
    def get(self,request,*args,**kwargs):
        username = request.user.username
        data=Complaint.objects.filter(username=username).order_by('status')
        return render(request,"usercomplaintview.html",{"data":data})

class OfficerList(View):
    def get(self,request,*args,**kwargs):
        is_officer=True
        data=CustUser.objects.filter(is_officer=is_officer)
        return render(request,"officerlist.html",{"data":data})
    
class CompliantEdit(View):
  def get(self,request,*args,**kwargs):
      id = kwargs.get("pk")
      obj = Complaint.objects.get(id=id)
      if obj.status== False:
        obj.status = True
        obj.save()
      else:
        obj.status = False
        obj.save()  
      return redirect("Offhome")
  
class Usercomplaintdelete(View):
  def get(self,request,*args,**kwargs):
    id = kwargs.get("pk")
    Complaint.objects.filter(id=id).delete()
    return redirect("usercomplaintlist")
  
class Complaintdetailview(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        obj=Complaint.objects.get(id=id)
        return render(request,"detailview.html",{'obj':obj})
class AnyoaddComplaint(View):
    def get(self,request,*args,**kwargs):
        form=AnyAddcomplaint()
        return render(request,"anycomp.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=AnyAddcomplaint(request.POST,files=request.FILES)
        if form.is_valid():
          form.save()
          form=AnyAddcomplaint()
          return redirect("index")
        else:
            return render(request, "anycomp.html", {"form": form})
        
class FeedbackformView(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        obj = Complaint.objects.get(id=id)
        form = FeedbackForm(instance=obj)
        return render(request,"feedback.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        obj = Complaint.objects.get(id=id)
        form = FeedbackForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("usercomplaintlist")
    
class FeedbackView(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        obj = Complaint.objects.filter(id=id)
        return render(request,"feedbackview.html",{"obj":obj})
class TermserviceView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"terms.html")
class DetailAddReport(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        obj = Complaint.objects.get(id=id)
        form = DetailForm(instance=obj)
        return render(request,"DetailReport.html",{"form":form})
       
    def post(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        obj = Complaint.objects.get(id=id)
        form = DetailForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            subject=obj.detail_head
            message=obj.detail_report
            # sender_mail= settings.EMAIL_HOST_USER
            recipient_email=[obj.email]
            print(recipient_email)
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_email, fail_silently=False)
                
            print('hlo')
            return redirect("Offhome")
class DetailViewReport(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        obj=Complaint.objects.filter(id=id)
        return render(request,'report_view.html',{'obj':obj})
    
class Department_DetailsView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        obj=Department.objects.filter(id=id)
        return render(request,"department_detail.html",{'obj':obj})



        


    

    







