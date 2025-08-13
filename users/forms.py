from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ContactForm



class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    ## configuracion requerida para mostrarlo de manera correcta
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    ## limpieza 
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user


class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ["customer_name", "customer_email", "message"]
        widgets = {
            "customer_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Tu nombre"}),
            "customer_email": forms.EmailInput(attrs={"class": "form-control","placeholder": "Correo electrónico"}),
            "message": forms.Textarea(attrs={"class": "form-control","placeholder": "Escribe tu mensaje","rows": 4}),
        }
        error_messages = {
            "customer_name": {
                "required": "El nombre es obligatorio.",
                "max_length": "El nombre es demasiado largo.",
            },
            "customer_email": {
                "required": "El correo es obligatorio.",
                "invalid": "Ingresa un correo válido.",
            },
            "message": {
                "required": "El mensaje no puede estar vacío.",
            },
        }

    def clean_customer_name(self):
        nombre = self.cleaned_data.get("customer_name", "").strip()
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return nombre

    def clean_message(self):
        mensaje = self.cleaned_data.get("message", "").strip()
        if len(mensaje) < 10:
            raise forms.ValidationError("El mensaje es demasiado corto. Sé más específico.")
        return mensaje