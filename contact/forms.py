from django import forms #Libreria de formularios django

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu nombre'}
    ), min_length=7, max_length=100)

    email = forms.EmailField(label="Correo electrónico", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu correo electrónico'}
    ), min_length=7, max_length=100)

    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows':4 , 'placeholder':'Escribe tu mensaje'}
    ), min_length=20, max_length=1000)
    