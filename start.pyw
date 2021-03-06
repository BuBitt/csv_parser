# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import prereq
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.Qt import QApplication
import sys
import csv
import os


def path(caminho):
    with open(caminho, encoding="utf-8") as csv_arq:
        leitor_csv = csv.DictReader(csv_arq)
        global csv_dict
        csv_dict = [dicio for dicio in leitor_csv][0].copy()
        #print(csv_dict)


class Cliente:

    def __init__(self, custo_por_resultado, valor_gasto, clique_no_link):
        self.__cus_por_res = custo_por_resultado
        self.__val_gasto = valor_gasto
        self.__clik_link = clique_no_link

    @property
    def custo_por_resultado(self):
        return self.__cus_por_res

    @property
    def valor_gasto(self):
        return self.__val_gasto

    @property
    def clique_no_link(self):
        return self.__clik_link
    
    def imprimir(self):
        texto = f"""Custo por resultado.............R$ {self.custo_por_resultado}
Valor gasto...........................R$ {self.valor_gasto}
Cliques no link únicos..........{self.clique_no_link}
"""
        return texto


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 260)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.anexarArquivo = QtWidgets.QPushButton(self.centralwidget)
        self.anexarArquivo.setObjectName("anexarArquivo")
        self.verticalLayout.addWidget(self.anexarArquivo)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.copiarArquivo = QtWidgets.QPushButton(self.centralwidget)
        self.copiarArquivo.setObjectName("copiarArquivo")
        self.verticalLayout.addWidget(self.copiarArquivo)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 632, 30))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSelecionar_arquivo = QtWidgets.QAction(MainWindow)
        self.actionSelecionar_arquivo.setObjectName("actionSelecionar_arquivo")
        self.menuArquivo.addAction(self.actionSelecionar_arquivo)
        self.menubar.addAction(self.menuArquivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Botões
        self.anexarArquivo.clicked.connect(self.anexar_arquivo)
        self.copiarArquivo.clicked.connect(self.copiar_texto)

        # Atalhos
        self.actionSelecionar_arquivo.triggered.connect(self.anexar_arquivo)
        self.qclip = QApplication.clipboard()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Catador deCVS"))
        self.anexarArquivo.setText(_translate("MainWindow", "Anexar arquivo (ctrl + o)"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Saída de Texto</span></p></body></html>"))
        self.copiarArquivo.setText(_translate("MainWindow", "Copiar"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.actionSelecionar_arquivo.setText(_translate("MainWindow", "Selecionar arquivo"))
        self.actionSelecionar_arquivo.setShortcut(_translate("MainWindow", "Ctrl+O"))
        
    
    def anexar_arquivo(self):
        file , check = QFileDialog.getOpenFileName(None, "Selecione o arquivo csv", "", "csv (*.csv);;All Files (*)")
        if check:
            path(file)
            cpr = round(float(csv_dict['Custo por resultados']), 2)
            vg = round(float(csv_dict['Valor gasto (BRL)']), 2)
            cl = csv_dict['Cliques no link únicos']
            cliente_1 = Cliente(cpr, vg, cl)

            global saida
            saida = cliente_1.imprimir()
            self.textEdit.setPlainText(saida)

    def copiar_texto(self):
        self.qclip.setText(saida)
        print("Copiado")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
