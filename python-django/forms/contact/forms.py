from django import forms


class ContactForm(forms.Form):
    
    nama_lengkap = forms.CharField()
    jenis_kelamin = forms.ChoiceField(
        choices=[
            ('P', 'Pria'),
            ('W', 'Wanita'),
        ]
    )
    tanggal_lahir = forms.DateTimeField(
        widget=forms.SelectDateWidget(
            years=range(1945, 2014, 1),
        )
    )
    email = forms.EmailField()
    alamat = forms.CharField()
    aggre = forms.BooleanField()
