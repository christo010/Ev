from django import forms
from EvApp.models import CustUser
from django.contrib.auth.forms import UserCreationForm
from EvApp.models import Department,Complaint

class Register(UserCreationForm):
    class Meta:
        model =CustUser
        fields = ['username','email','first_name','last_name','password1','password2']

class OfficerSignin(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class signin(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class Addform(forms.ModelForm):
    class Meta:
        model=Department
        fields= '__all__'

class Addcomplaint(forms.ModelForm):
    class Meta:
        model=Complaint
        fields= ['complaint_description','department','email','address','image','place']
        widgets = {
            'complaint_description': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
            'address': forms.Textarea(attrs={'rows': 5, 'cols': 40}),  # Customizing the widget for complaint_description field
        }

class AnyAddcomplaint(forms.ModelForm):
    class Meta:
        model=Complaint
        fields= ['username','complaint_description','department','image','place']
    def __init__(self, *args, **kwargs):
        super(AnyAddcomplaint, self).__init__(*args, **kwargs)
        self.fields['username'].initial = 'Anonymous User'
        self.fields['username'].widget.attrs['readonly'] = True  # Make username field readonly
        # self.fields['username'].widget.attrs['disabled'] = True  # For ensuring compatibility with older browsers
        widgets = {
            'complaint_description': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
            'address': forms.Textarea(attrs={'rows': 5, 'cols': 40}),  # Customizing the widget for complaint_description field
        }
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Complaint 
        fields = ['feedback']
        widgets = {
            'feedback':forms.Textarea(attrs={'rows' : 5 , 'cols' : 40})
        }
class DetailForm(forms.ModelForm):
    class Meta:
        model = Complaint 
        fields = ['detail_head','detail_report']
        widgets = {
            'detail_report':forms.Textarea(attrs={'rows' : 5 , 'cols' : 40})
        }





