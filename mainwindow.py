from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
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

        self.ui.actionAbrir.triggered.connect(self.action_Abrir_Archivo)
        self.ui.actionGuardar.triggered.connect(self.action_Guardar_Archivo)
        self.ui.MostrarTabla_PushButton.clicked.connect(self.mostrar_tabla)
        self.ui.Buscar_PushButton.clicked.connect(self.buscar_id)
        
    @Slot()
    def buscar_id(self):
        id = self.ui.Buscar_LineEdit.text()

        encontrado = False

        for vuelo in self.aeropuerto:
            if id == vuelo.id:
                self.ui.Tablita_TableWidget.clear()
                self.ui.Tablita_TableWidget.setRowCount(1)

                id_widget = QTableWidgetItem(vuelo.id)
                origen_widget = QTableWidgetItem(vuelo.origen)
                destino_widget = QTableWidgetItem(vuelo.destino)
                peso_widget = QTableWidgetItem(str(vuelo.peso))

                self.ui.Tablita_TableWidget.setItem(0, 0, id_widget)
                self.ui.Tablita_TableWidget.setItem(0, 1, origen_widget)
                self.ui.Tablita_TableWidget.setItem(0, 2, destino_widget)
                self.ui.Tablita_TableWidget.setItem(0, 3, peso_widget)

                encontrado = True

                return
            if not encontrado:
                QMessageBox.warning(
                    self,
                    "Atencion",
                    f'El avion con el identificador "{id}" no fue encontrado'
                )


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

    @Slot()
    def mostrar_tabla(self):
        self.ui.Tablita_TableWidget.setColumnCount(4)

        headers = ["ID", "Origen", "Destino", "Peso"]

        self.ui.Tablita_TableWidget.setHorizontalHeaderLabels(headers)
        self.ui.Tablita_TableWidget.setRowCount(len(self.aeropuerto))

        row = 0
        for vuelo in self.aeropuerto:
            id_widget = QTableWidgetItem(vuelo.id)
            origen_widget = QTableWidgetItem(vuelo.origen)
            destino_widget = QTableWidgetItem(vuelo.destino)
            peso_widget = QTableWidgetItem(str(vuelo.peso))

            self.ui.Tablita_TableWidget.setItem(row, 0, id_widget)
            self.ui.Tablita_TableWidget.setItem(row, 1, origen_widget)
            self.ui.Tablita_TableWidget.setItem(row, 2, destino_widget)
            self.ui.Tablita_TableWidget.setItem(row, 3, peso_widget)

            row += 1