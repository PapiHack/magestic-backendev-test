from django import forms
from ..models import Employe

class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ['nom', 'prenom', 'fonction', 'date_de_naissance', 'photo_de_profil']

    def __init__(self, *args, **kwargs):
        super(EmployeForm, self).__init__(*args, **kwargs)
        self.fields['date_de_naissance'].widget.attrs.update({'placeholder' : 'Ex: JJ/MM/AA ou JJ/MM/AAAA'})
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class' : 'form-control'})