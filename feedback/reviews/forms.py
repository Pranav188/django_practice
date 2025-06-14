from django import forms

class reviewForm(forms.Form):
    user_name = forms.CharField(label="tell me your goddamn name")