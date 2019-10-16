from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class student_signup_form(UserCreationForm):
	ID_No = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Student ID No.' }),required=True,max_length=30)
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter first name'}),required=True,max_length=30)
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter last name'}),required=True,max_length=30)
	email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email ID'}),required=True,max_length=30)
	department = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter department'}),required=True,max_length=30)
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),required=True,max_length=30)
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),required=True,max_length=30)
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}),required=True,max_length=30)

	class Meta:
		model=User
		fields=('ID_No','first_name','last_name','email','department','username','password1','password2')

	def clean_confirm_password(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password != confirm_password:
			raise forms.ValidationError("Password Mismatch")
		return confirm_password

	

	
	

class teacher_signup_form(UserCreationForm):
	ID_No = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Teacher ID No.' }),required=True,max_length=30)
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter first name'}),required=True,max_length=30)
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter last name'}),required=True,max_length=30)
	email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email ID'}),required=True,max_length=30)
	department = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter department'}),required=True,max_length=30)
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),required=True,max_length=30)
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),required=True,max_length=30)
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}),required=True,max_length=30)

	class Meta:
		model=User
		fields=('ID_No','first_name','last_name','email','department','username','password1','password2')

	def clean_confirm_password(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password != confirm_password:
			raise forms.ValidationError("Password Mismatch")
		return confirm_password


class UserLoginForm(forms.Form):
	username = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),required=True,max_length=30)
	password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),required=True,max_length=30)


class DocumentForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title'}),required=True,max_length=30)
	#document = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}),required=True,max_length=30)
	message = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter message'}),required=True,max_length=30)

	class Meta:
		model = Document
		fields = ('title', 'document', 'message' )

class UserEditForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )





class Student_Proctor_Form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}),required=True,max_length=30)
    contact_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    dept = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    father_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    mother_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    mobile_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    parent_occu = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    parent_income = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    parent_qual = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    current_cgpa = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    avg_cgpa = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    ssc_marks = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    hsc_marks = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    stu_ach = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)

    
    class Meta:
        model = student
        fields = (
            'name',
            'email',
            'contact_no',
            'dept',
            'address',
            'father_name',
            'mother_name',
            'mobile_no',
            'parent_occu',
            'parent_income',
            'parent_qual',
            'current_cgpa',
            'avg_cgpa',
            'ssc_marks',
            'hsc_marks',
            'stu_ach',
        )

class Stud(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),required=True,max_length=30)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','readonly':'readonly'}),required=True,max_length=30)
    contact_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    dept = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    father_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    mother_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    mobile_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    parent_occu = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    parent_income = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    parent_qual = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    current_cgpa = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    avg_cgpa = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    ssc_marks = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    hsc_marks = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
    stu_ach = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)

    
    class Meta:
        model = student
        fields = (
            'name',
            'email',
            'contact_no',
            'dept',
            'address',
            'father_name',
            'mother_name',
            'mobile_no',
            'parent_occu',
            'parent_income',
            'parent_qual',
            'current_cgpa',
            'avg_cgpa',
            'ssc_marks',
            'hsc_marks',
            'stu_ach',
        )

class Student_update_Form1(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),required=True,max_length=30)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','readonly':'readonly'}),required=True,max_length=30)
    contact_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),required=True,max_length=30)
    dept = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),required=True,max_length=30)
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),required=True,max_length=30)
    father_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),required=True,max_length=30)
    mother_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),required=True,max_length=30)
    mobile_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),required=True,max_length=30)
    parent_occu = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),required=True,max_length=30)
    parent_income = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),required=True,max_length=30)
    parent_qual = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),required=True,max_length=30)
    current_cgpa = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),required=True,max_length=30)
    avg_cgpa = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),required=True,max_length=30)
    ssc_marks = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),required=True,max_length=30)
    hsc_marks = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),required=True,max_length=30)
    stu_ach = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),required=True,max_length=30)

    
    class Meta:
        model = student
        exclude = ('created',)