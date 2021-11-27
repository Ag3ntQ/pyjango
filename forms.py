from django import forms
from .models import member

class Myform(forms.ModelForm):
	class Meta:
		model=member
		fields=["Name","Age","Class"]
		label={"Name":"Name","Age":"Age","Class":"Class"}