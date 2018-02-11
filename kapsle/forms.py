from django import forms
from .models import UserCoin, Coin, IgnoreCoin
from django.contrib.auth.models import User

#from django.utils.safestring import mark_safe


#class CustomField(forms.ModelChoiceField):
#
#    def label_from_instance(self, obj):
#        return mark_safe("<img src='%s'/>" % obj.image.url)


class UserCoinCreateForm(forms.ModelForm):
    #coin = forms.ModelChoiceField(widget=forms.HiddenInput(),
    #                                queryset=Coin.objects.all(), empty_label=None)

    class Meta:
        model = UserCoin
        fields = [
            'types',
            'kind',
            'condition',
            ]

#        widgets = {
#            'coin': forms.HiddenInput
#        }

#attrs={'class': 'input-hidden'}

class IgnoreCoinCreateForm(forms.ModelForm):
    owner = forms.ModelChoiceField(widget=forms.HiddenInput(), queryset=User.objects.all(), empty_label=None)
    #coin = forms.ModelChoiceField(widget=forms.HiddenInput(), queryset=Coin.objects.all(), empty_label=None)

    class Meta:
        model = IgnoreCoin
        fields = [
            'owner',
            ]

#        widgets = {
#            'ignored_by': forms.HiddenInput
#            }
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.fields['ignored_by'].queryset = User.objects.all()
# show_hidden_initial=True,