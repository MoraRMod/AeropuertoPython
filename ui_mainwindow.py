# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 652)
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionGuardar_2 = QAction(MainWindow)
        self.actionGuardar_2.setObjectName(u"actionGuardar_2")
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionAbrir_2 = QAction(MainWindow)
        self.actionAbrir_2.setObjectName(u"actionAbrir_2")
        self.actionGuardar_3 = QAction(MainWindow)
        self.actionGuardar_3.setObjectName(u"actionGuardar_3")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ID_LineEdit = QLineEdit(self.groupBox)
        self.ID_LineEdit.setObjectName(u"ID_LineEdit")

        self.gridLayout.addWidget(self.ID_LineEdit, 0, 1, 1, 1)

        self.ID_Label = QLabel(self.groupBox)
        self.ID_Label.setObjectName(u"ID_Label")

        self.gridLayout.addWidget(self.ID_Label, 0, 0, 1, 1)

        self.Destino_Label = QLabel(self.groupBox)
        self.Destino_Label.setObjectName(u"Destino_Label")

        self.gridLayout.addWidget(self.Destino_Label, 6, 0, 1, 1)

        self.Origen_LineEdit = QLineEdit(self.groupBox)
        self.Origen_LineEdit.setObjectName(u"Origen_LineEdit")

        self.gridLayout.addWidget(self.Origen_LineEdit, 2, 1, 1, 1)

        self.Origen_Label = QLabel(self.groupBox)
        self.Origen_Label.setObjectName(u"Origen_Label")

        self.gridLayout.addWidget(self.Origen_Label, 2, 0, 1, 1)

        self.Peso_Label = QLabel(self.groupBox)
        self.Peso_Label.setObjectName(u"Peso_Label")

        self.gridLayout.addWidget(self.Peso_Label, 4, 0, 1, 1)

        self.Peso_SpinBox = QSpinBox(self.groupBox)
        self.Peso_SpinBox.setObjectName(u"Peso_SpinBox")

        self.gridLayout.addWidget(self.Peso_SpinBox, 4, 1, 1, 1)

        self.Destino_LineEdit = QLineEdit(self.groupBox)
        self.Destino_LineEdit.setObjectName(u"Destino_LineEdit")

        self.gridLayout.addWidget(self.Destino_LineEdit, 6, 1, 1, 1)

        self.Agregar_Final_PushButton = QPushButton(self.groupBox)
        self.Agregar_Final_PushButton.setObjectName(u"Agregar_Final_PushButton")

        self.gridLayout.addWidget(self.Agregar_Final_PushButton, 9, 0, 1, 2)

        self.Agregar_Inicio_PushButton = QPushButton(self.groupBox)
        self.Agregar_Inicio_PushButton.setObjectName(u"Agregar_Inicio_PushButton")

        self.gridLayout.addWidget(self.Agregar_Inicio_PushButton, 10, 0, 1, 2)

        self.Mostrar_PushButton = QPushButton(self.groupBox)
        self.Mostrar_PushButton.setObjectName(u"Mostrar_PushButton")
        self.Mostrar_PushButton.setMouseTracking(False)
        self.Mostrar_PushButton.setAutoFillBackground(False)
        self.Mostrar_PushButton.setCheckable(False)
        self.Mostrar_PushButton.setAutoRepeat(False)
        self.Mostrar_PushButton.setAutoExclusive(False)
        self.Mostrar_PushButton.setAutoDefault(False)
        self.Mostrar_PushButton.setFlat(False)

        self.gridLayout.addWidget(self.Mostrar_PushButton, 11, 0, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.Salida_PlainTextEdit = QPlainTextEdit(self.centralwidget)
        self.Salida_PlainTextEdit.setObjectName(u"Salida_PlainTextEdit")

        self.gridLayout_2.addWidget(self.Salida_PlainTextEdit, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir_2)
        self.menuArchivo.addAction(self.actionGuardar_3)

        self.retranslateUi(MainWindow)

        self.Mostrar_PushButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.actionGuardar_2.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.actionAbrir_2.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir_2.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar_3.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar_3.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Vuelo", None))
        self.ID_Label.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.Destino_Label.setText(QCoreApplication.translate("MainWindow", u"Destino", None))
        self.Origen_Label.setText(QCoreApplication.translate("MainWindow", u"Origen", None))
        self.Peso_Label.setText(QCoreApplication.translate("MainWindow", u"Peso", None))
        self.Agregar_Final_PushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al Final", None))
        self.Agregar_Inicio_PushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al Inicio", None))
        self.Mostrar_PushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

