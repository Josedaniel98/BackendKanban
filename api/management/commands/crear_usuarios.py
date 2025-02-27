from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Crea usuarios automáticamente"

    def handle(self, *args, **kwargs):
        usuarios = [
            {"username": "usuario1", "email": "usuario1@example.com", "password": "password123"},
            {"username": "admin", "email": "admin@example.com", "password": "adminpassword", "is_staff": True, "is_superuser": True},
        ]

        for datos in usuarios:
            if User.objects.filter(username=datos["username"]).exists():
                self.stdout.write(self.style.WARNING(f"⚠️ El usuario '{datos['username']}' ya existe."))
                continue

            usuario = User.objects.create_user(
                username=datos["username"],
                email=datos["email"],
                password=datos["password"]
            )
            usuario.is_staff = datos.get("is_staff", False)
            usuario.is_superuser = datos.get("is_superuser", False)
            usuario.save()

            self.stdout.write(self.style.SUCCESS(f"✅ Usuario '{datos['username']}' creado exitosamente."))

