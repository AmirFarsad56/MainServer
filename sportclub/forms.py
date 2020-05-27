from sportclub.models import SportClubModel
from django import forms
from django.contrib.gis import forms as Gforms
from leaflet.forms.widgets import LeafletWidget
from django.core import validators



class SportClubForm(forms.ModelForm):
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = SportClubModel
        fields = ('phone_number','address','info','picture','location','sportclub_name','company_phone_number',)
        widgets = {
            'address': forms.Textarea(attrs={'id':'textarea1','class': 'materialize-textarea','style': "height: 100px"}),
            'info': forms.Textarea(attrs={'class': 'materialize-textarea','style': "height: 100px"}),
            'location': LeafletWidget(),
            'phone_number': forms.TextInput(attrs={'placeholder':'09121234567 مثال',}),
        }


class MessageForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea','style': "height: 100px"}))
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])


class EmailForm(forms.Form):
    subject = forms.CharField()
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea','style': "height: 100px"}))
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])


class BankInfoForm(forms.ModelForm):
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = SportClubModel
        fields = ('bankaccount_ownername','bankaccount_accountnumber',
                  'bankaccount_cardnumber',
                  'bankaccount_bankname')
        widgets = {
            'bankaccount_ownername': forms.TextInput(attrs={'id':'bankaccount_ownername'},),
            'bankaccount_accountnumber': forms.TextInput(attrs={'id':'bankaccount_accountnumber'},),
            'bankaccount_cardnumber': forms.TextInput(attrs={'id':'bankaccount_cardnumber'},),
            'bankaccount_bankname': forms.TextInput(attrs={'id':'bankaccount_bankname'},),
        }


class SportClubUpdateForm(forms.ModelForm):
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def __init__(self, *args, **kwargs):
        super(SportClubUpdateForm, self).__init__(*args, **kwargs)
        self.fields['picture'].required = False
    class Meta():
        model = SportClubModel
        fields = ('phone_number','address','info','picture','company_phone_number','sportclub_name')
        widgets = {
            'address': forms.Textarea(attrs={'id':'textarea1','class': 'materialize-textarea','style': "height: 100px"}),
            'info': forms.Textarea(attrs={'id':'info','class': 'materialize-textarea','style': "height: 100px"}),
            'picture': forms.FileInput(attrs={},),
            'phone_number': forms.TextInput(attrs={'id':'phone_number'},),
            'company_phone_number': forms.TextInput(attrs={'id':'company_phone_number'},),
            'sportclub_name': forms.TextInput(attrs={'id':'sportclub_name'},),
        }


class TermsAndConditionsForm(forms.ModelForm):
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = SportClubModel
        fields = ('terms_and_conditions',)
        widgets = {
            'terms_and_conditions': forms.Textarea(attrs={'id':'textarea1','class': 'materialize-textarea','style': "height: 100px"}),
        }
