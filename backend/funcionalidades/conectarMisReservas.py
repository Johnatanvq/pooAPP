import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QRegularExpressionValidator
from backend.classes.reserva import Reservas
from backend.funcionalidades.conectarEspacios import espaciosGUI
from backend.funcionalidades.conectarNuevoUsuario import nuevoUsuarioGUI
from backend.funcionalidades.conectarMaterias import materiaGUI
# from backend.funcionalidades.conectarMenuPrincipal import menuPrincipalGUI as MenuPrincipalGui
# from conectarLogin import loginGUI
#import bcrypt #hashes para encriptar las contraseñas, se puede dejar para más adelante

class misReservasGUI(QMainWindow):
    def __init__(self, cedula_usuario, id_materia):
        super().__init__()
        uic.loadUi("../pooAPP/frontend/vistas/misReservas/misReservas.ui", self)
        self.cedula_usuario = cedula_usuario  # La cédula del usuario logueado se recibe al inicializar
        self.id_materia = id_materia
        self.reserva = Reservas()  # Instanciar la clase que gestiona las reservas
        self.cargarReservas()
        self.bt_home_mm.clicked.connect(self.menuPrincipalGUI)
        self.bt_reservas_mm.clicked.connect(self.misReservas)
        self.bt_espacios_mm.clicked.connect(self.espacios)
        self.bt_usuarios_mm.clicked.connect(self.usuarios)
        self.bt_configuraciones_mm.clicked.connect(self.materias)

    def cargarReservas(self):
        try:
            # Obtener las reservas del usuario por su cédula
            reservas = self.reserva.obtenerReservasPorUsuario(self.cedula_usuario)
            
            # Refrescar la tabla
            self.TablaReservas.setRowCount(0)
            
            # Cargar la información en la tabla
            for reserva in reservas:
                fila = self.TablaReservas.rowCount()
                self.TablaReservas.insertRow(fila)
                
                # Asignar los datos a las columnas correspondientes
                self.TablaReservas.setItem(fila, 0, QTableWidgetItem(reserva['cedula']))  # Cédula usuario
                self.TablaReservas.setItem(fila, 1, QTableWidgetItem(reserva['descripcion']))  # Descripción
                self.TablaReservas.setItem(fila, 2, QTableWidgetItem(reserva['fecha_inicio'].strftime("%Y-%m-%d %H:%M")))  # Fecha_inicio
                self.TablaReservas.setItem(fila, 3, QTableWidgetItem(reserva['fecha_final'].strftime("%Y-%m-%d %H:%M")))  # Fecha_final

                # Agregar botón de eliminar
                btn_eliminar = QPushButton('Eliminar')
                btn_eliminar.clicked.connect(lambda ch, cedula=reserva['cedula'], descripcion=reserva['descripcion'], fecha_inicio=reserva['fecha_inicio'], fecha_final=reserva['fecha_final']: 
                                            self.eliminarReserva(cedula, descripcion, fecha_inicio, fecha_final))

                # Se crea un widget para añadir el botón de eliminar a la tabla
                widget = QWidget()
                layout = QHBoxLayout()
                layout.addWidget(btn_eliminar)
                layout.setAlignment(btn_eliminar, Qt.AlignCenter)
                widget.setLayout(layout)
                self.TablaReservas.setCellWidget(fila, 4, widget)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudieron cargar las reservas: {str(e)}")

    def eliminarReserva(self, cedula, descripcion, fecha_inicio, fecha_final):
        """
        Función para eliminar una reserva por sus valores únicos.
        """
        confirm = QMessageBox.question(self, "Confirmar eliminación", "¿Estás seguro de que deseas eliminar esta reserva?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if confirm == QMessageBox.Yes:
            try:
                self.reserva.eliminarReserva(cedula, descripcion, fecha_inicio, fecha_final)
                QMessageBox.information(self, "Éxito", "Reserva eliminada correctamente.")
                self.cargarReservas()  # Recargar la tabla después de eliminar
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo eliminar la reserva: {str(e)}")
       
    def menuPrincipalGUI(self):
        from backend.funcionalidades.conectarMenuPrincipal import menuPrincipalGUI
        self.close()
        self.login_window = menuPrincipalGUI(self.cedula_usuario, self.id_materia)
        self.login_window.show()
        
    def misReservas(self):
        from backend.funcionalidades.conectarCalendario import calendarioGUI
        self.close()
        self.login_window = calendarioGUI(self.cedula_usuario, self.id_materia)
        self.login_window.show()
    
    def espacios(self):
        self.close()
        self.login_window = espaciosGUI(self.cedula_usuario, self.id_materia)
        self.login_window.show()
        
    def usuarios(self):
        self.close()
        self.login_window = nuevoUsuarioGUI(self.cedula_usuario, self.id_materia)
        self.login_window.show()

    def materias(self):
        self.close()
        self.login_window = materiaGUI(self.cedula_usuario, self.id_materia)
        self.login_window.show()

    def cerrarSesion(self):
        from backend.funcionalidades.conectarLogin import loginGUI
        #se cierra la conexión a la base de datos desde la clase Usuario
        if hasattr(self.nuevoUsuario, 'cursor') and self.nuevoUsuario.cursor:
            self.nuevoUsuario.cursor.close()
        if hasattr(self.nuevoUsuario, 'conexion') and self.nuevoUsuario.conexion:
            self.nuevoUsuario.conexion.close()
        print("Conexión a la base de datos cerrada")
        
        #redirigir login
        self.close()
        self.login_window = loginGUI()  # Instanciar la ventana de login
        self.login_window.show()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = misReservasGUI()
    GUI.show()
    sys.exit(app.exec_())