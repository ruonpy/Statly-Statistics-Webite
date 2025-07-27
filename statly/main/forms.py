from django import forms

class NumberForm(forms.Form):
    numbers = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "For example: 5 7 2 5"})
    )