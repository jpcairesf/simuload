# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/joaocaires/Documentos/Projetos/Pessoal/Python/simuload/simuload/user_interface/original_design/novo_transformador.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NovoTransformador(object):
    def setupUi(self, NovoTransformador):
        NovoTransformador.setObjectName("NovoTransformador")
        NovoTransformador.resize(400, 282)
        self.buttonBox = QtWidgets.QDialogButtonBox(NovoTransformador)
        self.buttonBox.setGeometry(QtCore.QRect(50, 240, 341, 32))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.descTransf = QtWidgets.QGroupBox(NovoTransformador)
        self.descTransf.setGeometry(QtCore.QRect(10, 0, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        self.descTransf.setFont(font)
        self.descTransf.setObjectName("descTransf")
        self.label = QtWidgets.QLabel(self.descTransf)
        self.label.setGeometry(QtCore.QRect(40, 20, 331, 20))
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(NovoTransformador)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 381, 181))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 40, 361, 132))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.nome_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.nome_label.setObjectName("nome_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nome_label)
        self.transf_nome = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transf_nome.sizePolicy().hasHeightForWidth())
        self.transf_nome.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.transf_nome.setFont(font)
        self.transf_nome.setObjectName("transf_nome")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.transf_nome)
        self.demanda_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.demanda_label.setObjectName("demanda_label")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.demanda_label)
        self.transf_demanda = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transf_demanda.sizePolicy().hasHeightForWidth())
        self.transf_demanda.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.transf_demanda.setFont(font)
        self.transf_demanda.setObjectName("transf_demanda")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.transf_demanda)
        self.transf_fornecimento = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transf_fornecimento.sizePolicy().hasHeightForWidth())
        self.transf_fornecimento.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        self.transf_fornecimento.setFont(font)
        self.transf_fornecimento.setObjectName("transf_fornecimento")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.transf_fornecimento)
        self.fornecimento_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.fornecimento_label.setObjectName("fornecimento_label")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.fornecimento_label)

        self.retranslateUi(NovoTransformador)
        self.buttonBox.accepted.connect(NovoTransformador.accept)
        self.buttonBox.rejected.connect(NovoTransformador.reject)
        QtCore.QMetaObject.connectSlotsByName(NovoTransformador)

    def retranslateUi(self, NovoTransformador):
        _translate = QtCore.QCoreApplication.translate
        NovoTransformador.setWindowTitle(_translate("NovoTransformador", "Novo Transformador"))
        self.descTransf.setTitle(_translate("NovoTransformador", "Transformador"))
        self.label.setText(_translate("NovoTransformador", "Transformador com demanda e fornecimento por hora"))
        self.groupBox.setTitle(_translate("NovoTransformador", "Parâmetros"))
        self.nome_label.setText(_translate("NovoTransformador", "Nome"))
        self.demanda_label.setText(_translate("NovoTransformador", "Demanda"))
        self.fornecimento_label.setText(_translate("NovoTransformador", "Fornecimento"))
