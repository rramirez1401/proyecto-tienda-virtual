from django.db import models
import uuid
from django.utils.text import slugify


## Modelo tabla Flan
class Flan(models.Model):
    flan_uuid = models.UUIDField("UUID", default=uuid.uuid4, editable=False)
    name = models.CharField("Nombre", max_length=64)
    description = models.TextField("Descripcion")
    price = models.DecimalField("Precio", max_digits=5, decimal_places=0)
    imagen = models.ImageField("Imagen", upload_to="productos/")
    slug = models.SlugField("Slug", unique=True, blank=True, editable=False)
    is_private = models.BooleanField("Privado", default=False)
    stock = models.PositiveIntegerField("Stock", default=0, help_text="Unidades disponibles")

## Genera automaticamente el slug a partir del nombre
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            count = 1
            while Flan.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            self.slug = slug
        super().save(*args, **kwargs)


