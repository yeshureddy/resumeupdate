from django import forms
from . models import extrafield,educ,contactdetails,workexp,skills


class Extrafieldform(forms.ModelForm):
	class Meta:
		model = extrafield
		fields = ['field_name','explanation']
		widgets ={
			'field_name' : forms.TextInput(attrs={'class':'form-control'}),
			'explanation' : forms.Textarea(attrs={'class':'form-control'})
		}

			
class Educationdetails(forms.ModelForm):
	class Meta:
		model = educ
		fields =['school_name','school_location','Degree','CGPA','Field_of_Study','Expected_year_of_grad']
		widgets = {
		'school_name' : forms.TextInput(attrs={'class':'form-control'}),
		'school_location' : forms.TextInput(attrs={'class':'form-control'}),
		'Degree' : forms.TextInput(attrs={'class':'form-control'}),
		'CGPA' : forms.TextInput(attrs={'class':'form-control'}),
		'Field_of_Study' : forms.TextInput(attrs={'class':'form-control'}),
		'Expected_year_of_grad' : forms.TextInput(attrs={'class':'form-control'}),
	}
		
		
class contactdetailsform(forms.ModelForm):
	class Meta:
		model = contactdetails
		fields ='__all__'
		widgets = {
		'author' : forms.TextInput(attrs={'class':'form-control'}),
		'resume_name' : forms.TextInput(attrs={'class':'form-control'}),
		'full_name' : forms.TextInput(attrs={'class':'form-control col'}),
		'position' : forms.TextInput(attrs={'class':'form-control col'}),
		'city' : forms.TextInput(attrs={'class':'form-control'}),
		'state' : forms.TextInput(attrs={'class':'form-control'}),
		'zipcode' : forms.TextInput(attrs={'class':'form-control'}),
		'phone' : forms.TextInput(attrs={'class':'form-control'}),
		'email' : forms.TextInput(attrs={'class':'form-control'}),
		'personal_profile' : forms.TextInput(attrs={'class':'form-control'}),
	}
	


class jobform(forms.ModelForm):
	class Meta:
		model = workexp
		fields ='__all__'
		widgets = {
		'author' : forms.TextInput(attrs={'class':'form-control'}),
		'resume_name' : forms.TextInput(attrs={'class':'form-control'}),
		'job_title' : forms.TextInput(attrs={'class':'form-control'}),
		'employer' : forms.TextInput(attrs={'class':'form-control'}),
		'city' : forms.TextInput(attrs={'class':'form-control'}),
		'state' : forms.TextInput(attrs={'class':'form-control'}),
		'jobdesc' : forms.TextInput(attrs={'class':'form-control'}),
	}


 #THE BELOW CODE IS ADDED BY SIRI.
class skilldetails(forms.ModelForm):
	class Meta:
		model=skills
		fields=['skill']
		widgets = {
			'skill' : forms.TextInput(attrs={'class':'form-control'})
		}

from django import forms
from .models import Resume_No
class Rform(forms.ModelForm):
    class Meta:
        model = Resume_No
        fields = ('name','author')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-group'}),
            'author' : forms.TextInput(attrs={'class':'form-group','value':'','id' :'a','type':'hidden'})
            }