import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_alma.settings')
django.setup()

User = get_user_model()
if not User.objects.filter(username='ExioAdmin').exists():
    User.objects.create_superuser('ExioAdmin', 'enfermeriaalmaycuidado@gmail.com', 'Exio1234!')
    print("Usuario de Alma y Cuidado creado con éxito")
else:
    print("El usuario ya existe")