from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.utils import ImageReader
import io

def generar_documento_alma(cliente, tipo_doc):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=LETTER)
    
    # Intentar poner el logo desde la carpeta static
    try:
        logo = ImageReader('static/logo.png')
        p.drawImage(logo, 450, 680, width=100, height=100, mask='auto')
    except:
        pass

    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, 750, "ALMA Y CUIDADO 24/7 SAS")
    p.setFont("Helvetica", 10)
    p.drawString(50, 735, "NIT: 902041644-0")
    p.drawString(50, 720, "Representante: Exio Torrealba")

    # Contenido dinámico
    if tipo_doc == 'COTIZACION':
        p.setFont("Helvetica-Bold", 12)
        p.drawString(50, 680, "PROPUESTA DE SERVICIOS DE ENFERMERÍA")
        p.setFont("Helvetica", 11)
        p.drawString(50, 650, f"PARA: {cliente.nombre_completo}")
        p.drawString(50, 630, f"Servicio seleccionado: {cliente.get_tipo_servicio_display()}")
        p.drawString(50, 610, f"Valor Mensual sugerido: ${cliente.valor_mensual:,.0f} COP")
    
    # Aquí puedes expandir para CONTRATO o CUENTA_COBRO
    
    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer