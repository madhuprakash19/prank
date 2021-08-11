from django import forms
from crush.models import CreateUser,PrankList

class CreateUserForm(forms.ModelForm):

    class Meta():
        model = CreateUser
        fields = ('name',)

        widgets = {
            'name':forms.TextInput(attrs={'class':'textinputclass'}),
        }

class PrankListForm(forms.ModelForm):

    class Meta():
        model = PrankList
        fields = ('yourName','crushName')
