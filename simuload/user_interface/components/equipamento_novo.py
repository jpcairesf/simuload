# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'original_design\novo_equipamento.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NovoEquipamento(object):
    def setupUi(self, NovoEquipamento):
        NovoEquipamento.setObjectName("NovoEquipamento")
        NovoEquipamento.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(NovoEquipamento)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.descEquip = QtWidgets.QGroupBox(NovoEquipamento)
        self.descEquip.setGeometry(QtCore.QRect(10, 10, 381, 51))
        self.descEquip.setObjectName("descEquip")
        self.label = QtWidgets.QLabel(self.descEquip)
        self.label.setGeometry(QtCore.QRect(10, 20, 361, 20))
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(NovoEquipamento)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 381, 161))
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 361, 119))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.nome_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.nome_label.setObjectName("nome_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nome_label)
        self.equip_nome = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.equip_nome.setObjectName("equip_nome")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.equip_nome)
        self.pot_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.pot_label.setObjectName("pot_label")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pot_label)
        self.equip_potencia = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.equip_potencia.setObjectName("equip_potencia")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.equip_potencia)
        self.fp_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.fp_label.setObjectName("fp_label")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.fp_label)
        self.equip_fp = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.equip_fp.setObjectName("equip_fp")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.equip_fp)
        self.uso_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.uso_label.setObjectName("uso_label")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.uso_label)
        self.equip_uso = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.equip_uso.setObjectName("equip_uso")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.equip_uso)

        self.retranslateUi(NovoEquipamento)
        self.buttonBox.accepted.connect(NovoEquipamento.accept)
        self.buttonBox.rejected.connect(NovoEquipamento.reject)
        QtCore.QMetaObject.connectSlotsByName(NovoEquipamento)

    def retranslateUi(self, NovoEquipamento):
        _translate = QtCore.QCoreApplication.translate
        NovoEquipamento.setWindowTitle(_translate("NovoEquipamento", "Novo Equipamento"))
        self.descEquip.setTitle(_translate("NovoEquipamento", "Equipamento"))
        self.label.setText(_translate("NovoEquipamento", "Equipamento elétrico/iluminação de um ambiente"))
        self.groupBox.setTitle(_translate("NovoEquipamento", "Parâmetros"))
        self.nome_label.setText(_translate("NovoEquipamento", "Nome"))
        self.pot_label.setText(_translate("NovoEquipamento", "Potência "))
        self.fp_label.setText(_translate("NovoEquipamento", "Fator de Potência"))
        self.uso_label.setText(_translate("NovoEquipamento", "Uso Diário"))
