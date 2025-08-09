from django import forms


class ContactFormForm(forms.Form):
    customer_name = forms.CharField(max_length=64, label="Nombre")
    customer_email = forms.EmailField(label="Correo")
    message = forms.CharField(max_length=2000, label="Mensaje")