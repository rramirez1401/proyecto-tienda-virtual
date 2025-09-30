from django.contrib.auth.forms import AuthenticationForm
# Formulario de login personalizado con mensajes en español
class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                "Esta cuenta está inactiva.", code="inactive"
            )

    def clean(self):
        try:
            return super().clean()
        except forms.ValidationError:
            # Elimina todos los errores generales y agrega solo el mensaje en español
            self._errors["__all__"] = self.error_class([
                "Usuario o contraseña incorrectos. Por favor, verifica tus datos."])
            return self.cleaned_data
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ContactForm



class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")

    error_messages = {
        "password_mismatch": "Las contraseñas no coinciden.",
        "username_exists": "El nombre de usuario ya está registrado.",
        "email_exists": "El correo electrónico ya está registrado.",
    }

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
        # Mensajes de error en español para los campos
        self.fields["password1"].error_messages["required"] = "La contraseña es obligatoria."
        self.fields["password2"].error_messages["required"] = "Debes repetir la contraseña."
        self.fields["username"].error_messages["required"] = "El nombre de usuario es obligatorio."
        self.fields["email"].error_messages["required"] = "El correo electrónico es obligatorio."
        self.fields["first_name"].error_messages["required"] = "El nombre es obligatorio."
        self.fields["last_name"].error_messages["required"] = "El apellido es obligatorio."

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(self.error_messages["password_mismatch"], code="password_mismatch")
        return password2

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