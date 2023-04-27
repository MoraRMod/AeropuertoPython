from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from aeropuerto import Aeropuerto
from vuelo import Vuelo

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.aeropuerto = Aeropuerto()

        self.ui = Ui_MainWindow()
        
        self.ui.setupUi(self)
        
        self.ui.Agregar_Final_PushButton.clicked.connect(self.click_agregar)
        self.ui.Agregar_Final_PushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.Mostrar_PushButton.clicked.connect(self.click_mostrar)

        self.ui.actionAbrir_2.triggered.connect(self.action_Abrir_Archivo)
        self.ui.actionGuardar_3.triggered.connect(self.action_Guardar_Archivo)
        
    @Slot()
    def action_Abrir_Archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]

        if self.aeropuerto.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo abrir el archivo." + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "No se pudo abrir el archivo." + ubicacion
            )

    @Slot()
    def action_Guardar_Archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]

        print(ubicacion)

        if self.aeropuerto.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo." + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "No se pudo crear el archivo." + ubicacion
            )

    @Slot()
    def click_mostrar(self):
        self.ui.Salida_PlainTextEdit.clear()
        self.ui.Salida_PlainTextEdit.insertPlainText(str(self.aeropuerto))

    @Slot()
    def click_agregar(self):
        id = self.ui.ID_LineEdit.text()
        origen = self.ui.Origen_LineEdit.text()
        destino = self.ui.Destino_LineEdit.text()
        peso = self.ui.Peso_SpinBox.value()
        
        vuelo = Vuelo(id, origen, destino, peso)
        self.aeropuerto.agregar_final(vuelo)
    
    @Slot()
    def click_agregar_inicio(self):
        id = self.ui.ID_LineEdit.text()
        origen = self.ui.Origen_LineEdit.text()
        destino = self.ui.Destino_LineEdit.text()
        peso = self.ui.Peso_SpinBox.value()

        vuelo = Vuelo(id, origen, destino, peso)
        self.aeropuerto.agregar_inicio(vuelo)