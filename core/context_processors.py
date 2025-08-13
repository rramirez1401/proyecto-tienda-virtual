from users.forms import RegisterForm, ContactFormModelForm
from django.contrib.auth.forms import AuthenticationForm

def contact_form_processor(request):
    return {"contact_form": ContactFormModelForm()}

def auth_forms(request):
    login_form = AuthenticationForm()
    for field in login_form.fields.values():
        field.widget.attrs["class"] = "form-control"
    register_form = RegisterForm()
    return {
        'login_form': login_form,
        'register_form': register_form,
    }