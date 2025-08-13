from django.db import models
import uuid

## Modelo tabla ContactForm
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField("UUID Contacto", default=uuid.uuid4, editable=False)
    customer_email = models.EmailField("Correo", max_length=50, blank=False, null=False, help_text="ejemplo@gmail.com")
    customer_name = models.CharField("Nombre", max_length=64)
    message = models.TextField("Descripcion")