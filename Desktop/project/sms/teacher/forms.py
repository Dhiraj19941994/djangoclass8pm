from django import forms
from teacher.models import Notice,FoundItem,results,TeacherPP

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ('notice_subject','notice_image')

class FoundItemForm(forms.ModelForm):
    class Meta:
        model = FoundItem
        fields = ('found_item_name','found_item_detail','found_item_image')

class AddResultForm(forms.ModelForm):
    class Meta:
        model =results
        fields =('microprocessor','digital_logic','maths','english','database','coa')

class TeacherPPForm(forms.ModelForm):
    class Meta:
        model = TeacherPP
        fields = ('pp',)
