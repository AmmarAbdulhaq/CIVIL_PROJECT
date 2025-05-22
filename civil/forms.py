from django import forms

class InputForm(forms.Form):
    opc = forms.FloatField(label='OPC')
    fa = forms.FloatField(label='FA')
    ggb = forms.FloatField(label='GGBS')
    sf = forms.FloatField(label='SF')
    cc = forms.FloatField(label='CC')
    nca = forms.FloatField(label='NCA')
    rca = forms.FloatField(label='RCA')
    nfa = forms.FloatField(label='NFA')
    rfa = forms.FloatField(label='RFA')
    sp = forms.FloatField(label='SP')
    wb = forms.FloatField(label='w/b')