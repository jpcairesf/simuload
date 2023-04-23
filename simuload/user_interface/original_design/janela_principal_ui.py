# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/joaocaires/Documentos/Projetos/Pessoal/Python/simuload/simuload/user_interface/original_design/janela_principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 150, 331, 420))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.equipamento_menu = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equipamento_menu.sizePolicy().hasHeightForWidth())
        self.equipamento_menu.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(16)
        self.equipamento_menu.setFont(font)
        self.equipamento_menu.setObjectName("equipamento_menu")
        self.verticalLayout.addWidget(self.equipamento_menu)
        self.carga_menu = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.carga_menu.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.carga_menu.sizePolicy().hasHeightForWidth())
        self.carga_menu.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(16)
        self.carga_menu.setFont(font)
        self.carga_menu.setIconSize(QtCore.QSize(16, 16))
        self.carga_menu.setObjectName("carga_menu")
        self.verticalLayout.addWidget(self.carga_menu)
        self.transformador_menu = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transformador_menu.sizePolicy().hasHeightForWidth())
        self.transformador_menu.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(16)
        self.transformador_menu.setFont(font)
        self.transformador_menu.setObjectName("transformador_menu")
        self.verticalLayout.addWidget(self.transformador_menu)
        self.nova_curva = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.nova_curva.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nova_curva.sizePolicy().hasHeightForWidth())
        self.nova_curva.setSizePolicy(sizePolicy)
        self.nova_curva.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(16)
        self.nova_curva.setFont(font)
        self.nova_curva.setIconSize(QtCore.QSize(16, 16))
        self.nova_curva.setObjectName("nova_curva")
        self.verticalLayout.addWidget(self.nova_curva)
        self.editar_curva = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editar_curva.sizePolicy().hasHeightForWidth())
        self.editar_curva.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(16)
        self.editar_curva.setFont(font)
        self.editar_curva.setObjectName("editar_curva")
        self.verticalLayout.addWidget(self.editar_curva)
        self.excluir_curva = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.excluir_curva.sizePolicy().hasHeightForWidth())
        self.excluir_curva.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(16)
        self.excluir_curva.setFont(font)
        self.excluir_curva.setObjectName("excluir_curva")
        self.verticalLayout.addWidget(self.excluir_curva)
        self.exportar_curva = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exportar_curva.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exportar_curva.sizePolicy().hasHeightForWidth())
        self.exportar_curva.setSizePolicy(sizePolicy)
        self.exportar_curva.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(16)
        self.exportar_curva.setFont(font)
        self.exportar_curva.setIconSize(QtCore.QSize(16, 16))
        self.exportar_curva.setObjectName("exportar_curva")
        self.verticalLayout.addWidget(self.exportar_curva)
        self.simular_curva = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.simular_curva.sizePolicy().hasHeightForWidth())
        self.simular_curva.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(16)
        self.simular_curva.setFont(font)
        self.simular_curva.setObjectName("simular_curva")
        self.verticalLayout.addWidget(self.simular_curva)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(350, -10, 20, 591))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(20, -20, 311, 171))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("/home/joaocaires/Documentos/Projetos/Pessoal/Python/simuload/simuload/user_interface/original_design/../../img/simuload-logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(False)
        self.logo.setObjectName("logo")
        self.titulo_curvas = QtWidgets.QLabel(self.centralwidget)
        self.titulo_curvas.setGeometry(QtCore.QRect(380, 0, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(14)
        self.titulo_curvas.setFont(font)
        self.titulo_curvas.setObjectName("titulo_curvas")
        self.curvaList = QtWidgets.QListWidget(self.centralwidget)
        self.curvaList.setGeometry(QtCore.QRect(380, 50, 411, 221))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(14)
        self.curvaList.setFont(font)
        self.curvaList.setObjectName("curvaList")
        self.transfList = QtWidgets.QListWidget(self.centralwidget)
        self.transfList.setGeometry(QtCore.QRect(380, 350, 411, 221))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(14)
        self.transfList.setFont(font)
        self.transfList.setObjectName("transfList")
        self.titulo_transf = QtWidgets.QLabel(self.centralwidget)
        self.titulo_transf.setGeometry(QtCore.QRect(380, 300, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(14)
        self.titulo_transf.setFont(font)
        self.titulo_transf.setObjectName("titulo_transf")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuEditar = QtWidgets.QMenu(self.menubar)
        self.menuEditar.setInputMethodHints(QtCore.Qt.ImhDialableCharactersOnly|QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhEmailCharactersOnly|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhLatinOnly|QtCore.Qt.ImhLowercaseOnly|QtCore.Qt.ImhUppercaseOnly|QtCore.Qt.ImhUrlCharactersOnly)
        self.menuEditar.setObjectName("menuEditar")
        self.menu_curva = QtWidgets.QMenu(self.menuEditar)
        self.menu_curva.setInputMethodHints(QtCore.Qt.ImhDialableCharactersOnly|QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhEmailCharactersOnly|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhLatinOnly|QtCore.Qt.ImhLowercaseOnly|QtCore.Qt.ImhUppercaseOnly|QtCore.Qt.ImhUrlCharactersOnly)
        self.menu_curva.setObjectName("menu_curva")
        MainWindow.setMenuBar(self.menubar)
        self.actionNova_Curva = QtWidgets.QAction(MainWindow)
        self.actionNova_Curva.setObjectName("actionNova_Curva")
        self.actionAbrir_Curva = QtWidgets.QAction(MainWindow)
        self.actionAbrir_Curva.setObjectName("actionAbrir_Curva")
        self.actionCurvas_Recentes = QtWidgets.QAction(MainWindow)
        self.actionCurvas_Recentes.setObjectName("actionCurvas_Recentes")
        self.actionSalvar_Curva = QtWidgets.QAction(MainWindow)
        self.actionSalvar_Curva.setObjectName("actionSalvar_Curva")
        self.action_csv = QtWidgets.QAction(MainWindow)
        self.action_csv.setObjectName("action_csv")
        self.action_xls = QtWidgets.QAction(MainWindow)
        self.action_xls.setObjectName("action_xls")
        self.action5m = QtWidgets.QAction(MainWindow)
        self.action5m.setCheckable(True)
        self.action5m.setObjectName("action5m")
        self.action30m = QtWidgets.QAction(MainWindow)
        self.action30m.setCheckable(True)
        self.action30m.setObjectName("action30m")
        self.action15m = QtWidgets.QAction(MainWindow)
        self.action15m.setCheckable(True)
        self.action15m.setObjectName("action15m")
        self.action1h = QtWidgets.QAction(MainWindow)
        self.action1h.setCheckable(True)
        self.action1h.setChecked(True)
        self.action1h.setObjectName("action1h")
        self.menu_curva.addAction(self.action5m)
        self.menu_curva.addAction(self.action15m)
        self.menu_curva.addAction(self.action30m)
        self.menu_curva.addAction(self.action1h)
        self.menuEditar.addAction(self.menu_curva.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SIMULOAD"))
        self.equipamento_menu.setText(_translate("MainWindow", "Equipamentos"))
        self.carga_menu.setText(_translate("MainWindow", "Cargas"))
        self.transformador_menu.setText(_translate("MainWindow", "Transformadores"))
        self.nova_curva.setText(_translate("MainWindow", "Nova Curva"))
        self.editar_curva.setText(_translate("MainWindow", "Editar Curva"))
        self.excluir_curva.setText(_translate("MainWindow", "Excluir Curva"))
        self.exportar_curva.setText(_translate("MainWindow", "Exportar Curva"))
        self.simular_curva.setText(_translate("MainWindow", "Simular Curva"))
        self.titulo_curvas.setText(_translate("MainWindow", "Selecione uma curva de carga:"))
        self.titulo_transf.setText(_translate("MainWindow", "Selecione um transformador:"))
        self.menuEditar.setTitle(_translate("MainWindow", "Configurações"))
        self.menu_curva.setTitle(_translate("MainWindow", "Curva"))
        self.actionNova_Curva.setText(_translate("MainWindow", "Nova Curva"))
        self.actionAbrir_Curva.setText(_translate("MainWindow", "Abrir Curva"))
        self.actionCurvas_Recentes.setText(_translate("MainWindow", "Curvas Recentes"))
        self.actionSalvar_Curva.setText(_translate("MainWindow", "Salvar Curva"))
        self.action_csv.setText(_translate("MainWindow", ".csv"))
        self.action_xls.setText(_translate("MainWindow", ".xls"))
        self.action5m.setText(_translate("MainWindow", "5 min"))
        self.action30m.setText(_translate("MainWindow", "30 min"))
        self.action15m.setText(_translate("MainWindow", "15 min"))
        self.action1h.setText(_translate("MainWindow", "1 hora"))