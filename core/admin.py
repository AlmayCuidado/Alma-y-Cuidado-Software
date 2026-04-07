from django.contrib import admin
from django.http import HttpResponse
from .models import Cliente, Paciente, Enfermero, Documento
from .utils import generar_documento_alma # <-- Nombre corregido aquí

admin.site.site_header = "Alma y Cuidado 24/7"

class PacienteInline(admin.TabularInline):
    model = Paciente
    extra = 1

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'numero_identificacion', 'telefono', 'email')
    inlines = [PacienteInline]
    actions = ['descargar_propuesta_pdf']

    @admin.action(description="Generar Propuesta/Cotización (PDF)")
    def descargar_propuesta_pdf(self, request, queryset):
        for cliente in queryset:
            buffer = generar_documento_alma(cliente, 'COTIZACION')
            response = HttpResponse(buffer, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="Cotizacion_{cliente.nombre_completo}.pdf"'
            return response

admin.site.register(Enfermero)
admin.site.register(Documento)