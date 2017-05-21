from django import forms
from .models import Feedback


class FeedbackAddForm(forms.ModelForm):
	email = forms.CharField(widget=forms.TextInput(attrs={'size': 20}))
	comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'cols': 60, 'style': 'resize: none;'}))

	class Meta:
		model = Feedback
		fields = ('name', 'subject','category','email','comment','is_read',)


class FeedbackForm(forms.ModelForm):

	comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'cols': 60, 'style': 'resize: none;'}))
	created_on = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'size': '38'}))

	class Meta:
		model = Feedback
		fields = '__all__'
