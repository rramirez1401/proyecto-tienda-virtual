# Proyecto Tienda Virtual (OnlyFlans)

Plataforma web para la venta y gestión de flanes premium, con carrito de compras, registro de usuarios y administración de productos. Permite a los usuarios explorar productos, agregar a carrito, reservar órdenes y pagar, mientras el administrador gestiona stock y pedidos.

🚀 Características principales
- Registro y autenticación de usuarios (Django auth).
- Registro con datos personales (nombre, apellido, email) y validación en español.
- Login con formulario personalizado y mensajes de error amigables.
- Catálogo público de productos (flanes) con filtros por visibilidad (`is_private=False`).
- Detalle de producto con URL amigable mediante slug.
- Gestión de stock para evitar sobreventa.
- Carrito/orden:
  - `Order` y `OrderItem` con estados `reserved`, `paid`, `cancelled`.
  - Reserva temporal de stock con tiempo de expiración configurable (`RESERVATION_TTL_MINUTES`).
  - Rol de administrador para revisar y procesar órdenes desde Django Admin.
- Área protegida (`/bienvenido/`) que muestra productos privados y públicos al usuario autenticado.
- Formulario de contacto funcional con validaciones y mensajes.

🛠️ Tecnologías utilizadas
- Backend: Django (Python)
- Base de datos: SQLite por defecto (pero compatible con PostgreSQL)
- Frontend: Django templates (HTML, CSS, JS), Bootstrap (en estilos del proyecto)
- Archivos estáticos: Django staticfiles
- Gestión de dependencias: `requirements.txt`
- Control de versiones: Git & GitHub

📂 Estructura del proyecto
```
proyecto-tienda-virtual/
├── cart/                # app de carrito y órdenes
│   ├── models.py
│   ├── views.py
│   ├── services.py
│   └── migrations/
├── core/                # middleware y context processors
├── users/               # app de usuarios y autenticación
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── templates/modals/
├── web/                 # app principal de productos
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── onlyflans/           # configuración Django (settings, urls, wsgi, asgi)
├── manage.py
├── requirements.txt
└── README.md
```

⚙️ Instalación y configuración
1. Clonar repositorio
```bash
git clone https://github.com/rramirez1401/proyecto-tienda-virtual.git
cd proyecto-tienda-virtual
```
2. Crear y activar entorno virtual
```bash
python3 -m venv .venv
source .venv/bin/activate
```
3. Instalar dependencias
```bash
pip install -r requirements.txt
```
4. Configurar variables de entorno
- Crear `.env` con al menos:
  - `SECRET_KEY` (Django)
  - `DEBUG=True` durante desarrollo
  - Configuración de DB si se usa PostgreSQL (opcional)

5. Migraciones
```bash
python manage.py migrate
```
6. Crear superusuario
```bash
python manage.py createsuperuser
```
7. Ejecutar servidor
```bash
python manage.py runserver
```
8. Acceder a la aplicación
- Público: `http://localhost:8000/`
- Admin: `http://localhost:8000/admin/`

📖 Uso de la aplicación
1. Registro de usuario en `/usuarios/registro/`.
2. Inicio de sesión en `/usuarios/iniciar_sesion/`.
3. Navegar catálogo y ver detalles.
4. Añadir productos al carrito (funcionalidad de órdenes y stock).
5. Completar la orden y el estado pasa de `reserved` a `paid`/`cancelled`.
6. Contacto desde formulario en la página principal.

🔮 Mejoras futuras (pueden añadirse conforme tu sugerencia)
- Dashboard completo para dueño/e-commerce con métricas, ventas, stock y órdenes.
- Roles avanzados: vendedor, cliente, admin con permisos diferenciados.
- Pago real con MercadoPago/Stripe.
- Gestión de productos privados compartidos por empresa/influencer.
- Notificaciones por email/SMS para estado de orden y stock bajo.
- Panel de administración mejorado (gráficos, filtros, reportes).
- Búsqueda y filtros de producto por categoría y precio.
- Internacionalización (i18n) y soporte de múltiples monedas.

🤝 Contribuciones
¡Bienvenidas! Para colaborar:
1. Haz un fork del proyecto.
2. Crea una rama (`git checkout -b feature/nombre`).
3. Haz commit de tus cambios (`git commit -m 'Descripción'`).
4. Haz push (`git push origin feature/nombre`).
5. Abre un Pull Request.

📜 Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente, mencionando al autor.

👨‍💻 Autor
Desarrollado por Raúl Ignacio Ramírez Sanhueza
- Repositorio principal: `rramirez1401/proyecto-tienda-virtual`
- Referencia secundaria: `raul-1601/proyecto-inmobiliario`
