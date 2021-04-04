from django import forms
from student.models import ClaimItem

class ClaimItemForm(forms.ModelForm):
    class Meta:
        model = ClaimItem
        fields =('claim',)
