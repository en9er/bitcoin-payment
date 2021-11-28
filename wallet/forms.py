from django import forms


class SendBtcForm(forms.Form):
    mnemonic = forms.CharField(max_length=256, label="Your mnemonic words")
    target_address = forms.CharField(max_length=256, label="Target address")
    amount = forms.FloatField(label="Amount")
