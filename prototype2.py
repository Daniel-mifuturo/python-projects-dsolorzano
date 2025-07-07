from fpdf import FPDF

class PrototipoPDF(FPDF):
    def header(self):
        if self.page_no() == 1:  # Solo en la portada
            self.image("logo_cardiso.png", 60, 20, 90)  # Logo grande, centrado
            self.ln(70)  # Espacio adicional debajo del logo

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.set_text_color(128)
        self.cell(0, 10, f"Página {self.page_no()}", align="C")

    def add_section(self, title, visual, description):
        self.set_font("Arial", "B", 14)
        self.set_text_color(0)
        self.cell(0, 10, title, ln=True)
        self.ln(2)
        
        # Visual
        self.set_font("Courier", "", 10)
        self.multi_cell(0, 6, visual)
        self.ln(2)
        
        # Descripción
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 8, description)
        self.ln(5)

# Crear PDF
pdf = PrototipoPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# 1. Portada
pdf.add_page()
pdf.set_font("Arial", "B", 20)
pdf.cell(0, 40, "Prototipo Visual para Cardiso S.A.", ln=True, align="C")
pdf.ln(10)
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Brenes Sánchez Jeaustin, Brenes Sánchez Kevin,", ln=True, align="C")
pdf.cell(0, 10, "y Solórzano Damaceno Daniel", ln=True, align="C")
pdf.ln(10)
pdf.set_font("Arial", "", 14)
pdf.cell(0, 10, "Profesor: Hernandez Mendoza Kevin", ln=True, align="C")
pdf.cell(0, 10, "Universidad Fidélitas", ln=True, align="C")

# 2. Sistema de autenticación
pdf.add_page()
pdf.add_section(
    "Sistema de Autenticación",
    """\
---------------------------------------------------------
| [ Iniciar Sesión ]                                    |
---------------------------------------------------------
| Usuario: [__________________________]                 |
| Contraseña: [______________________]                  |
---------------------------------------------------------
""",
    """\
Función: Asegurar que solo usuarios autorizados accedan al contenido.
Utilizar servicios como AWS Cognito para federar identidades y manejar roles de usuario.
Prototipo: Interfaz que permita inicio de sesión y configuración de permisos.
"""
)

# 3. Transcripción y traducción automática
pdf.add_page()
pdf.add_section(
    "Transcripción y Traducción Automática",
    """\
---------------------------------------------------------
| [Subir Audio]  [Seleccionar Idioma]                   |
---------------------------------------------------------
| Resultados:                                           |
| [Texto Traducido]  [Audio Traducido]                  |
---------------------------------------------------------
""",
    """\
Función: Convertir audio en texto y traducirlo automáticamente a diferentes idiomas.
Utilizar herramientas como AWS Transcribe y AWS Polly para generar transcripciones y audios en diversos idiomas.
Prototipo: Flujo donde un audio se convierte en texto y luego en diferentes idiomas.
"""
)

# 4. Almacenamiento en la nube
pdf.add_page()
pdf.add_section(
    "Almacenamiento en la Nube",
    """\
---------------------------------------------------------
| [Grabaciones]  [Descargar en MP3]  [Descargar en MP4] |
---------------------------------------------------------
| Espacio utilizado: 75%                               |
---------------------------------------------------------
""",
    """\
Función: Almacenar las grabaciones de las conferencias, accesibles desde cualquier dispositivo.
Prototipo: Panel con opciones para descargar grabaciones en formatos como MP3 y MP4.
"""
)

# 5. Sala virtual para eventos
pdf.add_page()
pdf.add_section(
    "Sala Virtual para Eventos",
    """\
---------------------------------------------------------
| SALA VIRTUAL                                          |
---------------------------------------------------------
| [Unirse al Evento]                                    |
| [Transmisión en Vivo]                                 |
---------------------------------------------------------
""",
    """\
Función: Permitir la transmisión en vivo, compatibilidad con múltiples plataformas y una interfaz sencilla para los clientes.
Prototipo: Página de ejemplo para seleccionar eventos y unirse a transmisiones en vivo.
"""
)

# 6. Reservas y contratación de servicios
pdf.add_page()
pdf.add_section(
    "Reservas y Contratación de Servicios",
    """\
---------------------------------------------------------
| Reservar Servicio                                     |
---------------------------------------------------------
| Idioma: [_________]                                   |
| Fecha:  [_________]                                   |
| Servicio: [_________]                                 |
---------------------------------------------------------
| [ Confirmar ]                                         |
---------------------------------------------------------
""",
    """\
Función: Facilitar la contratación en línea con generación automática de contratos electrónicos.
Prototipo: Formulario interactivo que permita elegir idioma, fecha y tipo de servicio.
"""
)

# 7. Pie de página / Contacto
pdf.add_page()
pdf.add_section(
    "Contacto y Redes",
    """\
---------------------------------------------------------
| CONTACTO                                              |
---------------------------------------------------------
| Email: eventos@cardiso.com                            |
| Teléfono: +1 234 567 8901                             |
| Web: www.cardiso.com                                  |
---------------------------------------------------------
""",
    """\
Para más información, visita nuestra página web o síguenos en nuestras redes sociales. Cardiso S.A. está comprometido con ofrecer soluciones modernas y accesibles para todos nuestros clientes.
"""
)

# Guardar archivo final
pdf.output("Prototipo_Plataforma_Eventos_COMPLETO.pdf")
