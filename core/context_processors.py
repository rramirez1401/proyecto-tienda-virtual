from web.forms import ContactFormModelForm
from users.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm

def contact_form_processor(request):
    return {"contact_form": ContactFormModelForm()}


def auth_forms(request):
    return {
        'login_form': AuthenticationForm(),
        'register_form': RegisterForm(),
    }