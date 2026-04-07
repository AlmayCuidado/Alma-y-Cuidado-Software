from django.db import models

class Cliente(models.Model):
    TIPOS_DOC = [
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
        ('NIT', 'NIT'),
        ('PAS', 'Pasaporte'),
    ]
    
    SERVICIOS = [
        ('8H', 'Prestación de servicios auxiliar de enfermería (8 Horas)'),
        ('12H', 'Prestación de servicios auxiliar de enfermería (12 Horas)'),
        ('24H', 'Prestación de servicios auxiliar de enfermería (24 Horas)'),
    ]
    
    DURACION = [
        ('DIAS', 'Días'),
        ('SEM', 'Semanas'),
        ('MES', 'Meses'),
        ('IND', 'Indefinido'),
    ]

    nombre_completo = models.CharField(max_length=200)
    tipo_documento = models.CharField(max_length=5, choices=TIPOS_DOC, default='CC')
    numero_identificacion = models.CharField(max_length=20, unique=True)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    
    tipo_servicio = models.CharField(max_length=5, choices=SERVICIOS)
    unidad_duracion = models.CharField(max_length=5, choices=DURACION, default='MES')
    cantidad_duracion = models.IntegerField(default=1)
    
    valor_diario = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    valor_semanal = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    valor_mensual = models.DecimalField(max_digits=10, decimal_places=0, default=0)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nombre_completo

class Paciente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="pacientes")
    nombre_paciente = models.CharField(max_length=200)
    tipo_documento = models.CharField(max_length=5, choices=Cliente.TIPOS_DOC, default='CC')
    numero_identificacion = models.CharField(max_length=20)
    direccion = models.TextField()
    condicion = models.TextField(verbose_name="Condición Médica")
    # Línea 60 corregida aquí abajo:
    parentesco = models.CharField(max_length=100, verbose_name="Relación con el Cliente")

    def __str__(self):
        return self.nombre_paciente

class Enfermero(models.Model):
    nombre = models.CharField(max_length=200)
    especialidad = models.CharField(max_length=100)
    cedula = models.CharField(max_length=50, unique=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.especialidad})"

class Documento(models.Model):
    TIPOS_DOC_SISTEMA = [
        ('CONTRATO', 'Contrato de Servicio'),
        ('COTIZACION', 'Cotización'),
        ('CUENTA_COBRO', 'Cuenta de Cobro'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPOS_DOC_SISTEMA)
    fecha_emision = models.DateField(auto_now_add=True)
    archivo_pdf = models.FileField(upload_to='documentos/', null=True, blank=True)

    def __str__(self):
        return f"{self.tipo} - {self.cliente.nombre_completo}"