from users.forms import RegisterForm, ContactFormModelForm
from users.forms import CustomAuthenticationForm

def contact_form_processor(request):
    return {"contact_form": ContactFormModelForm()}

def auth_forms(request):
    login_form = CustomAuthenticationForm()
    for field in login_form.fields.values():
        field.widget.attrs["class"] = "form-control"
    register_form = RegisterForm()
    return {
        'login_form': login_form,
        'register_form': register_form,
    }