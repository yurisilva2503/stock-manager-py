from PySide6.QtWidgets import (QTreeWidgetItem, QMainWindow, QApplication, QMessageBox, QDialog,
                               QTableWidget, QTableWidgetItem, QVBoxLayout, QDialogButtonBox,
                               QInputDialog)

from PySide6.QtCore import Qt
from PySide6.QtGui import QRegularExpressionValidator, QIcon
from ui_login import Ui_Tela_Login
from ui_telaprincipal import Ui_MainWindow
import sys
from database import DataBase
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import locale
from queue import Queue
from PIL import Image


class Login(QMainWindow, Ui_Tela_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.w = None
        self.users = None
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle('Login - PyStock')
        iconapp = QIcon('imagens/logo_junta3.png')
        self.setWindowIcon(iconapp)
        self.btn_login.clicked.connect(self.checkLogin)

    def checkLogin(self):
        self.users = DataBase()
        self.users.conecta()
        authentication = self.users.check_user(self.txt_user.text(), self.txt_password.text())
        if authentication == "Administrador" or authentication == "Usuário":
            self.w = MainWindow(authentication.lower())
            if authentication.lower() == "usuário":
                self.w.btn_cadastrarusuario.setVisible(False)
            self.w.show()
            self.close()
        else:
            QMessageBox.warning(self, "Erro de autenticação", "Usuário ou senha inválidos.")
            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle('Erro ao acessar')
                msg.setText(f'Login ou senha inválidos \n \n Tentativa: {self.tentativas + 1} de 3 ')
                msg.exec()
                self.tentativas += 1
            if self.tentativas == 3:
                self.users.close_connection()
                sys.exit(0)

    def sair_sistema(self):
        if self.parent():
            self.parent().login = None
        self.close()


class EditItemDialog(QDialog):
    def __init__(self, item_data):
        super(EditItemDialog, self).__init__()
        self.item_data = item_data
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle('Editar Item')
        layout = QVBoxLayout()
        table = QTableWidget()
        table.setColumnCount(14)
        table.setHorizontalHeaderLabels(
            ['Codigo_Produto', 'Nf_e', 'Serie', 'Data_Emissao', 'Chave_de_Acesso', 'Cnpj_Emitente', 'Emitente',
             'Descricao', 'Unidade', 'Preco', 'Quantidade', 'Total', 'Data_Entrada', 'Avaria'])
        table.setRowCount(1)
        for i, value in enumerate(self.item_data):
            item = QTableWidgetItem(str(value))
            table.setItem(0, i, item)
        layout.addWidget(table)

        buttons = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)

        save_button = buttons.button(QDialogButtonBox.Save)
        cancel_button = buttons.button(QDialogButtonBox.Cancel)

        save_button.setStyleSheet('''
            QPushButton {
                background-color: rgb(0, 0, 0);
                color: rgb(255, 255, 255);
                font: 75 11pt "MS Shell Dlg 2";
            }

            QPushButton:hover {
                background-color: rgb(85, 255, 127);
                color: black;
            }
        ''')

        cancel_button.setStyleSheet('''
            QPushButton {
                background-color: rgb(0, 0, 0);
                color: rgb(255, 255, 255);
                font: 75 11pt "MS Shell Dlg 2";
            }

            QPushButton:hover {
                background-color: rgb(85, 255, 127);
                color: black;

            }
        ''')

        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
        self.setFixedSize(839, 150)
        self.setLayout(layout)

    def getEditedData(self):
        edited_data = []
        table = self.findChild(QTableWidget)
        for column in range(14):
            item = table.item(0, column)
            edited_data.append(item.text())
        return edited_data


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user) -> None:
        super(MainWindow, self).__init__()
        self.user = user
        self.setupUi(self)
        self.setWindowTitle('Gerenciamento - PyStock')
        iconapp = QIcon('imagens/logo_junta3.png')
        self.setWindowIcon(iconapp)

        self.login = None

        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_tables.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_table))
        self.btn_contato.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contato))
        self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))
        self.btn_cadastrarusuario.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro))

        self.cad_btncadastro.clicked.connect(self.subscribe_user)
        self.btn_cadastrarmerc.clicked.connect(self.cadastrar_produtos)
        self.btn_sair.clicked.connect(self.sair_sistema)
        self.btn_excluirmerc.clicked.connect(self.excluir_produto)
        self.btn_gerarsaida.clicked.connect(self.gerar_saida)
        self.btn_gerarestorno.clicked.connect(self.gerar_retorno)
        self.btn_gerargrafico.clicked.connect(self.graphic)
        self.txt_search.textChanged.connect(self.buscar_referencia_geral)
        self.line_busca.textChanged.connect(self.buscar_referencia)
        self.btn_editaritem.clicked.connect(self.editaritem)
        self.btn_gerarexcel.clicked.connect(self.excel_file)
        self.fila = Queue()
        self.btn_removertopofila.clicked.connect(self.removertopofila)
        self.btn_zerarsaidas.clicked.connect(self.zerar_saidas)
        self.btn_excluirsaida.clicked.connect(self.excluir_saida)
        self.buscar_produtos()

        numeros_validador = QRegularExpressionValidator("^[0-9]*$")
        preco_validator = QRegularExpressionValidator("^\\d{1,3}(\\.\\d{3})*(,\\d{0,2})?$")

        self.line_codprod.setValidator(numeros_validador)
        self.line_nfe.setValidator(numeros_validador)
        self.line_serienfe.setValidator(numeros_validador)
        self.line_chavedeacessonfe.setValidator(numeros_validador)
        self.line_cnpjemitente.setValidator(numeros_validador)
        self.line_quantidade.setValidator(numeros_validador)
        self.line_preco.setValidator(preco_validator)

    def sair_sistema(self):
        if not self.login:
            self.login = Login()
        self.login.show()
        self.close()

    def subscribe_user(self):
        nome = self.cad_nome.text()
        user = self.cad_usuario.text().strip()
        password = self.cad_senha.text().strip()
        access = self.cb_perfil.currentText()

        if nome == "" or user == "" or password == "" or access == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('Preencha todas as informações')
            msg.setText('Por favor, preencha todos os campos obrigatórios.')
            msg.exec_()
            return None

        if self.cad_senha.text() != self.cad_confirmarsenha.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('Senhas divergentes')
            msg.setText('As senhas não coincidem.')
            msg.exec_()
            return None

        db = DataBase()
        db.conecta()

        if db.check_user_exists(user):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('Usuário já existe')
            msg.setText('O usuário já está registrado. Por favor, escolha outro usuário.')
            msg.exec_()
            db.close_connection()
            return None

        db.insert_user(nome, user, password, access)
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('Cadastro de Usuário')
        msg.setText('Cadastro realizado com sucesso!')
        msg.exec()

        self.cad_nome.setText("")
        self.cad_usuario.setText("")
        self.cad_senha.setText("")
        self.cad_confirmarsenha.setText("")

    def cadastrar_produtos(self):
        codprod = self.line_codprod.text()
        nfe = self.line_nfe.text()
        serienfe = self.line_serienfe.text()
        chavedeacesso = self.line_chavedeacessonfe.text()
        cnpjemitente = self.line_cnpjemitente.text()

        if (
                not codprod
                or not nfe
                or not serienfe
                or not chavedeacesso
                or not cnpjemitente
        ):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('Preencha todas as informações')
            msg.setText('Por favor, preencha todos os campos obrigatórios.')
            msg.exec_()
            return

        if (
                len(codprod) != 14
                or len(nfe) != 9
                or len(serienfe) != 3
                or len(chavedeacesso) != 40
                or len(cnpjemitente) != 14
        ):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('Informações inválidas')
            msg.setText('Por favor, verifique os campos e preencha com informações válidas.')
            msg.exec_()
            return

        db = DataBase()
        db.conecta()

        preco_text = self.line_preco.text().replace(".", "").replace(",", ".")
        quantidade_text = self.line_quantidade.text()

        preco = float(preco_text)
        quantidade = float(quantidade_text)
        total = preco * quantidade
        total_formatted = locale.format_string('%.2f', total, grouping=True)

        date_entradaproduto = self.date_entradaproduto.date().toString("dd/MM/yyyy")
        date_emissaonfs = self.date_emissaonfs.date().toString("dd/MM/yyyy")

        listaprodutos = (
            codprod,
            nfe,
            serienfe,
            date_emissaonfs,
            chavedeacesso,
            cnpjemitente,
            self.line_emitente.text(),
            self.line_descprod.text(),
            self.line_unidade.text(),
            self.line_preco.text(),
            self.line_quantidade.text(),
            total_formatted,
            date_entradaproduto,
            self.cb_avaria.currentText(),
        )

        resp = db.register_products(*listaprodutos)

        self.line_codprod.clear()
        self.line_nfe.clear()
        self.line_serienfe.clear()
        self.line_chavedeacessonfe.clear()
        self.line_cnpjemitente.clear()
        self.line_emitente.clear()
        self.line_descprod.clear()
        self.line_unidade.clear()
        self.line_preco.clear()
        self.line_quantidade.clear()
        self.cb_avaria.setCurrentIndex(-1)

        if resp == 'Ok':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro Realizado!")
            msg.setText("Cadastro de produto realizado com sucesso!")
            msg.exec()
            self.buscar_produtos()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Cadastro não realizado!")
            msg.setText("O cadastro de produto não foi realizado com sucesso!")
            msg.exec()

        db.close_connection()

    def buscar_produtos(self):
        db = DataBase()
        db.conecta()

        produtos = db.select_all_products()

        self.tree_estoque.clear()

        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

        for produto in produtos:
            codigo = produto[0]
            quantidade = int(produto[10]) if produto[10] else 0

            items = self.tree_estoque.findItems(codigo, Qt.MatchExactly, 0)

            if items:
                item = items[0] 
                self.tree_estoque.indexFromItem(item)
                item.setText(12, str(quantidade))
            else:
                item = QTreeWidgetItem(self.tree_estoque)
                item.setText(0, codigo)
                item.setText(1, produto[1])
                item.setText(2, produto[2])
                item.setText(3, produto[3])
                item.setText(4, produto[4])
                item.setText(5, produto[5])
                item.setText(6, produto[6])
                item.setText(7, produto[7])
                item.setText(8, produto[8])
                item.setText(9, produto[9])
                item.setText(10, str(quantidade))

                preco_text = float(produto[9].replace(".", "").replace(",", "."))
                quantidade_text = float(produto[10])
                preco = float(preco_text)
                quantidade = float(quantidade_text)
                total = preco * quantidade
                total_formatted = locale.format_string('%.2f', total, grouping=True)

                item.setText(11, str(f'R${total_formatted}'))
                item.setText(12, produto[12])
                item.setText(13, produto[13])

                for i in range(0, 13):
                    self.tree_estoque.resizeColumnToContents(i)

        produtos_saida = db.select_all_saida()
        self.tree_saida.clear()

        for produto_saida in produtos_saida:
            item_saida = QTreeWidgetItem(self.tree_saida)
            item_saida.setText(0, str(produto_saida[0]))
            item_saida.setText(1, str(produto_saida[1]))
            item_saida.setText(2, str(produto_saida[2]))
            item_saida.setText(3, str(produto_saida[3]))
            item_saida.setText(4, str(produto_saida[4]))
            item_saida.setText(5, str(produto_saida[5]))
            item_saida.setText(6, str(produto_saida[6]))
            item_saida.setText(7, str(produto_saida[7]))
            item_saida.setText(8, str(produto_saida[8]))
            item_saida.setText(9, str(produto_saida[9]))
            item_saida.setText(10, str(produto_saida[10]))

            preco_text = float(produto_saida[9].replace(".", "").replace(",", "."))
            quantidade_text = float(produto_saida[10])
            preco_m = float(preco_text)
            quantidade_m = float(quantidade_text)
            total = preco_m * quantidade_m
            total_formatted = locale.format_string('%.2f', total, grouping=True)

            item_saida.setText(11, str(f'R${total_formatted}'))
            item_saida.setText(12, str(produto_saida[12]))
            item_saida.setText(13, str(produto_saida[13]))
            item_saida.setText(14, str(produto_saida[14]))

            for i in range(0, 14):
                self.tree_saida.resizeColumnToContents(i)

        produtos_geral = db.select_all_geral()
        self.tree_geral.clear()
        contador = len(produtos_geral)

        for produto_geral in reversed(produtos_geral):
            self.fila.put(produto_geral)

        while not self.fila.empty():
            produtos_geral = self.fila.get()
            item_geral = QTreeWidgetItem(self.tree_geral)
            item_geral.setText(0, str(contador))
            item_geral.setText(1, str(produtos_geral[0]))
            item_geral.setText(2, str(produtos_geral[1]))
            item_geral.setText(3, str(produtos_geral[2]))
            item_geral.setText(4, str(produtos_geral[3]))
            item_geral.setText(5, str(produtos_geral[4]))
            item_geral.setText(6, str(produtos_geral[5]))
            item_geral.setText(7, str(produtos_geral[6]))
            item_geral.setText(8, str(produtos_geral[7]))
            item_geral.setText(9, str(produtos_geral[8]))
            item_geral.setText(10, str(produtos_geral[9]))

            preco_text = float(produtos_geral[9].replace(".", "").replace(",", "."))
            quantidade_text = float(produtos_geral[10])
            preco_m = float(preco_text)
            quantidade_m = float(quantidade_text)
            total = preco_m * quantidade_m
            total_formatted = locale.format_string('%.2f', total, grouping=True)

            item_geral.setText(11, str(produtos_geral[10]))
            item_geral.setText(12, str(f'R${total_formatted}'))
            item_geral.setText(13, str(produtos_geral[12]))
            item_geral.setText(14, str(produtos_geral[13]))
            item_geral.setText(15, str(produtos_geral[14]))
            contador -= 1

            for i in range(0, 15):
                self.tree_geral.resizeColumnToContents(i)

        db.close_connection()

    def update_produtos(self):
        dados = []
        update_dados = []
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

        for row in range(self.tree_estoque.topLevelItemCount()):
            item = self.tree_estoque.topLevelItem(row)
            for column in range(self.tree_estoque.columnCount()):
                dados.append(item.text(column))

            update_dados.append(dados)
            dados = []

        db = DataBase()
        db.conecta()

        for prod in update_dados:
            codigoproduto = prod[0]
            nfe = prod[1]
            serie = prod[2]
            data_emissao = prod[3]
            chave_de_acesso = prod[4]
            cnpj_emitente = prod[5]
            emitente = prod[6]
            descricao = prod[7]
            unidade = prod[8]
            preco = prod[9]
            quantidade = prod[10]

            preco_text = float(prod[9].replace(".", "").replace(",", "."))
            quantidade_text = float(prod[10])
            preco_m = float(preco_text)
            quantidade_m = float(quantidade_text)
            total = preco_m * quantidade_m
            total_formatted = locale.format_string('%.2f', total, grouping=True)

            data_entrada = prod[12]
            avaria = prod[13]
            db.update_products(codigoproduto, nfe, serie, data_emissao, chave_de_acesso, cnpj_emitente, emitente,
                               descricao, unidade, preco, quantidade, total_formatted, data_entrada, avaria)
        db.close_connection()

        self.buscar_produtos()

    def excluir_produto(self):
        item = self.tree_estoque.currentItem()

        msg_box = QMessageBox()
        msg_box.setWindowTitle("Excluir Produto")
        msg_box.setText("Você realmente deseja excluir esse produto?")

        msg_box.setStyleSheet('''
                            QPushButton {
                                background-color: rgb(0, 0, 0);
                                color: rgb(255, 255, 255);
                            }

                            QPushButton:hover {
                                background-color: rgb(85, 255, 127);
                                color: black;
                            }

                            QLabel {
                            qproperty-alignment: AlignCenter;
                            font-size: 20px;
                            }
                        ''')

        msg_box.addButton("Sim", QMessageBox.AcceptRole)
        msg_box.addButton("Não", QMessageBox.RejectRole)

        msg_box.exec()
        if msg_box.clickedButton().text() == 'Sim':
            if item:
                codprod = item.text(0)
                db = DataBase()
                db.conecta()
                resp = db.delete_products(codprod)
                db.close_connection()
                if resp == 'Produto excluído com sucesso!':
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Produto excluido com sucesso!")
                    msg.exec()
                    self.buscar_produtos()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setWindowTitle('Erro ao excluir produto')
                    msg.setText(resp)
                    msg.exec()

    def gerar_saida(self):
        item = self.tree_estoque.currentItem()

        if item:
            codigoproduto = item.text(0)
            nfe = item.text(1)
            serie = item.text(2)
            data_emissao = item.text(3)
            chave_de_acesso = item.text(4)
            cnpj_emitente = item.text(5)
            emitente = item.text(6)
            descricao = item.text(7)
            unidade = item.text(8)
            preco = item.text(9)
            quantidade_estoque = int(item.text(10))

            preco_text = float(preco.replace(".", "").replace(",", "."))
            quantidade_text = float(quantidade_estoque)
            preco_m = float(preco_text)
            quantidade_m = float(quantidade_text)
            total = preco_m * quantidade_m
            total_formatted = locale.format_string('%.2f', total, grouping=True)

            data_entrada = item.text(12)
            avaria = item.text(13)

            dialog = QInputDialog(self)
            dialog.setWindowTitle("Quantidade de Saída")
            dialog.setLabelText("Informe a quantidade a ser retirada:")
            dialog.setInputMode(QInputDialog.IntInput)
            dialog.setIntMinimum(1)
            dialog.setIntMaximum(quantidade_estoque)
            dialog.setIntValue(1)
            dialog.setOkButtonText("OK")
            dialog.setCancelButtonText("Cancelar")

            if dialog.exec() == QInputDialog.Accepted:
                quantidade = dialog.intValue()

                quantidade_estoque -= quantidade

                data_saida, ok = QInputDialog.getText(self, "Data de Saída", "Informe a data de saída do produto:")
                if ok:
                    db = DataBase()
                    db.conecta()

                    resp = db.register_saida(codigoproduto, nfe, serie, data_emissao, chave_de_acesso, cnpj_emitente,
                                             emitente, descricao, unidade, preco, quantidade, total_formatted,
                                             data_entrada, avaria,
                                             data_saida)

                    db.register_geral(codigoproduto, nfe, serie, data_emissao, chave_de_acesso, cnpj_emitente,
                                      emitente, descricao, unidade, preco, quantidade, total_formatted,
                                      data_entrada, avaria,
                                      data_saida)

                    if resp == 'Ok':
                        item_saida = QTreeWidgetItem(self.tree_saida)
                        item_saida.setText(0, codigoproduto)
                        item_saida.setText(1, nfe)
                        item_saida.setText(2, serie)
                        item_saida.setText(3, data_emissao)
                        item_saida.setText(4, chave_de_acesso)
                        item_saida.setText(5, cnpj_emitente)
                        item_saida.setText(6, emitente)
                        item_saida.setText(7, descricao)
                        item_saida.setText(8, unidade)
                        item_saida.setText(9, preco)
                        item_saida.setText(10, str(quantidade))

                        preco_text = float(preco.replace(".", "").replace(",", "."))
                        quantidade_text = float(quantidade)
                        preco_m = float(preco_text)
                        quantidade_m = float(quantidade_text)
                        total = preco_m * quantidade_m
                        total_formatted = locale.format_string('%.2f', total, grouping=True)

                        item_saida.setText(11, str(f'R${total_formatted}'))
                        item_saida.setText(12, data_entrada)
                        item_saida.setText(13, avaria)
                        item_saida.setText(14, data_saida)

                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Saída de Produto")
                        msg.setText("Saída de produto registrada com sucesso!")
                        msg.exec()

                        item.setText(10, str(quantidade_estoque))

                        db.update_products(codigoproduto, nfe, serie, data_emissao, chave_de_acesso, cnpj_emitente,
                                           emitente, descricao, unidade, preco, quantidade_estoque, total_formatted,
                                           data_entrada, avaria)

                        if quantidade_estoque == 0:
                            db.remove_produto(codigoproduto)
                            self.update_produtos()
                            self.buscar_produtos()
                            db.close_connection()
                        else:
                            for i in range(self.tree_estoque.topLevelItemCount()):
                                item_estoque = self.tree_estoque.topLevelItem(i)
                                if item_estoque.text(0) == codigoproduto:
                                    item_estoque.setText(10, str(quantidade_estoque))
                                    db.close_connection()
                                    break

                    else:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setWindowTitle("Erro na Saída")
                        msg.setText("Não foi possível registrar a saída do produto.")
                        msg.exec()
                        db.close_connection()
                self.buscar_produtos()

    def gerar_retorno(self):
        item_saida = self.tree_saida.currentItem()
        if item_saida:
            codigoproduto = item_saida.text(0)
            nfe = item_saida.text(1)
            serie = item_saida.text(2)
            data_emissao = item_saida.text(3)
            chave_de_acesso = item_saida.text(4)
            cnpj_emitente = item_saida.text(5)
            emitente = item_saida.text(6)
            descricao = item_saida.text(7)
            unidade = item_saida.text(8)
            preco = item_saida.text(9)
            quantidade_saida = int(item_saida.text(10))

            preco_text = float(preco.replace(".", "").replace(",", "."))
            quantidade_text = float(quantidade_saida)
            preco_m = float(preco_text)
            quantidade_m = float(quantidade_text)
            total = preco_m * quantidade_m
            total_formatted = locale.format_string('%.2f', total, grouping=True)

            data_entrada = item_saida.text(12)
            avaria = item_saida.text(13)
            data_saida = item_saida.text(14)

            dialog = QInputDialog(self)
            dialog.setWindowTitle("Quantidade de Retorno")
            dialog.setLabelText("Informe a quantidade a ser gerada de volta para o estoque:")
            dialog.setInputMode(QInputDialog.IntInput)
            dialog.setIntMinimum(1)
            dialog.setIntMaximum(quantidade_saida)
            dialog.setIntValue(1)
            dialog.setOkButtonText("OK")
            dialog.setCancelButtonText("Cancelar")

            if dialog.exec() == QInputDialog.Accepted:
                quantidade_retorno = dialog.intValue()

                quantidade_saida -= quantidade_retorno
                item_saida.setText(10, str(quantidade_saida))

                db = DataBase()
                db.conecta()

                item_estoque = None
                for i in range(self.tree_estoque.topLevelItemCount()):
                    item = self.tree_estoque.topLevelItem(i)
                    if item.text(0) == codigoproduto:
                        item_estoque = item
                        break

                if item_estoque:
                    quantidade_estoque = int(item_estoque.text(10))
                    quantidade_estoque += quantidade_retorno
                    item_estoque.setText(10, str(quantidade_estoque))
                    db.update_products(codigoproduto, nfe, serie, data_emissao, chave_de_acesso, cnpj_emitente,
                                       emitente, descricao, unidade, preco, quantidade_estoque, total_formatted,
                                       data_entrada,
                                       avaria)
                else:
                    item_estoque = QTreeWidgetItem(self.tree_estoque)
                    item_estoque.setText(0, codigoproduto)
                    item_estoque.setText(1, nfe)
                    item_estoque.setText(2, serie)
                    item_estoque.setText(3, data_emissao)
                    item_estoque.setText(4, chave_de_acesso)
                    item_estoque.setText(5, cnpj_emitente)
                    item_estoque.setText(6, emitente)
                    item_estoque.setText(7, descricao)
                    item_estoque.setText(8, unidade)
                    item_estoque.setText(9, preco)
                    item_estoque.setText(10, str(quantidade_retorno))
                    item_estoque.setText(11, str(f'R${total_formatted}'))
                    item_estoque.setText(12, data_entrada)
                    item_estoque.setText(13, avaria)

                    db.register_products(codigoproduto, nfe, serie, data_emissao, chave_de_acesso, cnpj_emitente,
                                         emitente, descricao, unidade, preco, quantidade_retorno, total_formatted,
                                         data_entrada, avaria)

                db.reduce_quantidade_saida(codigoproduto, quantidade_retorno, data_saida)
                db.reduce_quantidade_geral(codigoproduto, quantidade_retorno, data_saida)

                if quantidade_saida == 0:
                    has_other_entries = False
                    for i in range(self.tree_saida.topLevelItemCount()):
                        item = self.tree_saida.topLevelItem(i)
                        if (
                                item.text(0) == codigoproduto
                                and item.text(14) == data_saida
                                and int(item.text(10)) > 0
                        ):
                            has_other_entries = True
                            break

                    if not has_other_entries:
                        self.tree_saida.takeTopLevelItem(
                            self.tree_saida.indexOfTopLevelItem(item_saida)
                        )
                        db.remove_saida(codigoproduto, data_saida)
                        db.remove_geral(codigoproduto, data_saida)

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Retorno de Produto")
                msg.setText("Retorno de produto registrado com sucesso!")
                msg.exec()
                db.close_connection()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Retorno Cancelado")
                msg.setText("O retorno de produto foi cancelado.")
                msg.exec()

        self.buscar_produtos()

    @staticmethod
    def graphic():
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Escolher Gráfico")
        msg_box.setText("Qual gráfico você deseja ver?")

        msg_box.setStyleSheet('''
                    QPushButton {
                        background-color: rgb(0, 0, 0);
                        color: rgb(255, 255, 255);
                    }

                    QPushButton:hover {
                        background-color: rgb(85, 255, 127);
                        color: black;
                    }

                    QLabel {
                    qproperty-alignment: AlignCenter;
                    font-size: 20px;
                    }
                ''')

        msg_box.addButton("Relação entre Estoque e Saida", QMessageBox.ActionRole)
        msg_box.addButton("Distribuição dos Produtos por Descrição", QMessageBox.ActionRole)
        msg_box.addButton(QMessageBox.Close)
        close_button = msg_box.button(QMessageBox.Close)
        close_button.setVisible(False)

        msg_box.exec()

        if msg_box.clickedButton().text() == "Relação entre Estoque e Saida":
            cnx = sqlite3.connect("system.db")
            estoque = pd.read_sql_query('SELECT * FROM products', cnx)
            saida = pd.read_sql_query("SELECT * FROM geral WHERE data_entrada != ''", cnx)
            estoque_qntd = pd.read_sql_query(
                'SELECT Descricao, CAST(Quantidade AS INTEGER) AS Quantidade FROM products', cnx)
            saida_qntd = pd.read_sql_query(
                "SELECT Descricao, CAST(Quantidade AS INTEGER) AS Quantidade FROM saida_produtos", cnx)

            estoque['Quantidade'] = estoque['Quantidade'].astype(int)
            saida['Quantidade'] = saida['Quantidade'].astype(int)
            estoque_qntd['Quantidade'] = estoque_qntd['Quantidade'].astype(int)
            saida_qntd['Quantidade'] = saida_qntd['Quantidade'].astype(int)

            estoque_sum = estoque['Quantidade'].sum()
            saida_sum = saida['Quantidade'].sum()
            estoque_qntd_sum = estoque_qntd['Quantidade'].sum()
            saida_qntd_sum = saida_qntd['Quantidade'].sum()

            colors = ['#459FD8', '#FD5458']
            labels = "Estoque", "Saídas"
            sizes = [estoque_sum, saida_sum]
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors=colors, wedgeprops={
                'edgecolor': 'white'})
            ax1.axis("equal")

            legenda = f"Estoque: {estoque_qntd_sum}"
            legenda2 = f"Saída: {saida_qntd_sum}"
            ax1.legend(loc='center left', bbox_to_anchor=(0.8, 0.0), title="Quantidade", labels=[legenda, legenda2])

            contador = 1
            nome_arquivo = f"graficos\\Relação_entre_Estoque_e_Saida{contador}.png"

            while os.path.exists(nome_arquivo):
                contador += 1
                nome_arquivo = f"graficos\\Relação_entre_Estoque_e_Saida{contador}.png"

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Gráfico")
            msg.setText("Gráfico de Relação entre Estoque e Saida gerado com sucesso na pasta de gráficos! ")
            msg.exec()
            plt.savefig(nome_arquivo)
            plt.close()
            imagem = Image.open(nome_arquivo)
            imagem.show()

        elif msg_box.clickedButton().text() == "Distribuição dos Produtos por Descrição":
            cnx = sqlite3.connect("system.db")

            estoque = pd.read_sql_query('SELECT Descricao, CAST(Quantidade AS INTEGER) AS Quantidade FROM products',
                                        cnx)
            estoque_descricao = estoque["Descricao"].tolist()
            estoque_quantidade = estoque["Quantidade"].tolist()

            saida = pd.read_sql_query(
                "SELECT Descricao, CAST(Quantidade AS INTEGER) AS Quantidade FROM geral WHERE data_entrada != ''", cnx)
            saida_descricao = saida["Descricao"].tolist()
            saida_quantidade = saida["Quantidade"].tolist()

            labels_estoque = estoque_descricao
            sizes_estoque = estoque_quantidade
            labels_saida = saida_descricao
            sizes_saida = saida_quantidade

            fig, axs = plt.subplots(1, 3, figsize=(12, 6))

            axs[0].barh(range(len(labels_estoque)), sizes_estoque, height=0.5, color='#459FD8')
            axs[0].set_yticks(range(len(labels_estoque)))
            axs[0].set_yticklabels(labels_estoque, fontsize=8) 
            axs[0].set_title("Estoque")

            axs[1].barh(range(len(labels_saida)), sizes_saida, height=0.5, color='#FD5458')
            axs[1].set_yticks(range(len(labels_saida)))
            axs[1].set_yticklabels(labels_saida, fontsize=8)
            axs[1].set_title("Saídas")

            ax2 = plt.subplot(1, 3, 3)
            descricao_estoque = "\n".join(
                [f"{descricao}: {quantidade}" for descricao, quantidade in zip(labels_estoque, sizes_estoque)])
            descricao_saida = "\n".join(
                [f"{descricao}: {quantidade}" for descricao, quantidade in zip(labels_saida, sizes_saida)])

            ax2.axis("off")

            fontsize = 8
            line_spacing = 1.2
            ax2.text(0, 0.5, f"Estoque:\n{descricao_estoque}\n\nSaídas:\n{descricao_saida}", fontsize=fontsize,
                     verticalalignment='center', linespacing=line_spacing)

            plt.tight_layout()

            contador = 1
            nome_arquivo = f"graficos\\Distribuicao_Produtos_por_Descricao{contador}.png"

            while os.path.exists(nome_arquivo):
                contador += 1
                nome_arquivo = f"graficos\\Distribuicao_Produtos_por_Descricao{contador}.png"
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Gráfico")
            msg.setText("Gráfico de Distribuição dos Produtos por Descrição gerado com sucesso na pasta gráficos! ")
            msg.exec()
            plt.savefig(nome_arquivo)
            plt.close()
            imagem = Image.open(nome_arquivo)
            imagem.show()

    def buscar_referencia(self):
        busca = self.line_busca.text()
        self.tree_estoque.clearSelection()

        if busca:
            for column in range(self.tree_estoque.columnCount()):
                items = self.tree_estoque.findItems(busca, Qt.MatchContains, column)
                if items:
                    self.tree_estoque.scrollToItem(items[0])
                    for item in items:
                        item.setSelected(True)
                    break
        else:
            self.tree_estoque.clearSelection()

    def buscar_referencia_geral(self):
        busca = self.txt_search.text()
        self.tree_geral.clearSelection()
        if busca:
            for column in range(self.tree_geral.columnCount()):
                items = self.tree_geral.findItems(busca, Qt.MatchContains, column)
                if items:
                    self.tree_geral.scrollToItem(items[0])
                    for item in items:
                        item.setSelected(True)
                    break
        else:
            self.tree_geral.clearSelection()

    def editaritem(self):
        item = self.tree_estoque.currentItem()
        if item:
            item_data = []
            for column in range(self.tree_estoque.columnCount()):
                item_data.append(item.text(column))

            dialog = EditItemDialog(item_data)
            if dialog.exec() == QDialog.Accepted:
                edited_data = dialog.getEditedData()
                for i, value in enumerate(edited_data):
                    item.setText(i, value)

                total = float(item.text(9).replace(".", "").replace(",", ".")) * float(item.text(10))
                total_formatado = locale.format_string('%.2f', total, grouping=True)
                item.setText(11, total_formatado)
                self.update_produtos()

    @staticmethod
    def excel_file():
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        relatorios_dir = os.path.join(os.getcwd(), "relatorios")

        if not os.path.exists(relatorios_dir):
            os.makedirs(relatorios_dir)

        cnx = sqlite3.connect('system.db')
        result = pd.read_sql_query("SELECT * FROM geral", cnx)
        result.to_excel(os.path.join(relatorios_dir, f"Resumo_geral_das_saidas_({current_date}).xlsx"),
                        sheet_name='geral', index=False)

        cnx2 = sqlite3.connect('system.db')
        result2 = pd.read_sql_query("SELECT * FROM products", cnx2)
        result2.to_excel(os.path.join(relatorios_dir, f"Resumo_geral_do_estoque_({current_date}).xlsx"),
                         sheet_name='products', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Relatório de Notas")
        msg.setText("Relatório gerado com sucesso!")
        msg.exec()

    def removertopofila(self):
        db = DataBase()
        db.conecta()
        produtos_geral = db.select_all_geral()

        if len(produtos_geral) == 0:
            print("A fila está vazia.")
            return

        ultimo_produto = produtos_geral[0]

        msg_box = QMessageBox()
        msg_box.setWindowTitle("Excluir Nº da Fila")
        msg_box.setText("Você realmente deseja excluir o primeiro (Nº1) item da fila de saidas?")

        msg_box.setStyleSheet('''
                QPushButton {
                background-color: rgb(0, 0, 0);
                color: rgb(255, 255, 255);
                }
                QPushButton:hover {	
                background-color: rgb(60, 60, 60);
                }
                QPushButton:pressed {	
                background-color: rgb(0, 0, 0);
                color: rgb(35, 35, 35);
                }
                QLabel {
                qproperty-alignment: AlignCenter;
                font-size: 18px;}''')

        msg_box.addButton("Sim", QMessageBox.AcceptRole)
        msg_box.addButton("Não", QMessageBox.RejectRole)

        msg_box.exec()
        if msg_box.clickedButton().text() == 'Sim':
            db.remove_geral(ultimo_produto[0], ultimo_produto[14])
            db.remove_saida(ultimo_produto[0], ultimo_produto[14])

            produtos_geral = db.select_all_geral()

            self.tree_geral.clear()
            contador = len(produtos_geral)
            for produto_geral in reversed(produtos_geral):
                item_geral = QTreeWidgetItem(self.tree_geral)
                item_geral.setText(0, str(contador))  # Adiciona a numeração na coluna "Nº"
                item_geral.setText(1, str(produto_geral[0]))
                item_geral.setText(2, str(produto_geral[1]))
                item_geral.setText(3, str(produto_geral[2]))
                item_geral.setText(4, str(produto_geral[3]))
                item_geral.setText(5, str(produto_geral[4]))
                item_geral.setText(6, str(produto_geral[5]))
                item_geral.setText(7, str(produto_geral[6]))
                item_geral.setText(8, str(produto_geral[7]))
                item_geral.setText(9, str(produto_geral[8]))
                item_geral.setText(10, str(produto_geral[9]))

                preco_text = float(produto_geral[9].replace(".", "").replace(",", "."))
                quantidade_text = float(produto_geral[10])
                preco_m = float(preco_text)
                quantidade_m = float(quantidade_text)
                total = preco_m * quantidade_m
                total_formatted = locale.format_string('%.2f', total, grouping=True)

                item_geral.setText(11, str(produto_geral[10]))
                item_geral.setText(12, str(f'R${total_formatted}'))
                item_geral.setText(13, str(produto_geral[12]))
                item_geral.setText(14, str(produto_geral[13]))
                item_geral.setText(15, str(produto_geral[14]))
                contador -= 1

                for i in range(0, 15):
                    self.tree_geral.resizeColumnToContents(i)
            self.buscar_produtos()
            db.close_connection()

    def excluir_saida(self):
        item = self.tree_saida.currentItem()

        msg_box = QMessageBox()
        msg_box.setWindowTitle("Excluir Saída")
        msg_box.setText("Você realmente deseja excluir essa saída?")

        msg_box.setStyleSheet('''
                            QPushButton {
                                background-color: rgb(0, 0, 0);
                                color: rgb(255, 255, 255);
                            }

                            QPushButton:hover {
                                background-color: rgb(85, 255, 127);
                                color: black;
                            }

                            QLabel {
                            qproperty-alignment: AlignCenter;
                            font-size: 20px;
                            }
                        ''')

        msg_box.addButton("Sim", QMessageBox.AcceptRole)
        msg_box.addButton("Não", QMessageBox.RejectRole)

        msg_box.exec()
        if msg_box.clickedButton().text() == 'Sim':
            if item:
                codprod = item.text(0)
                data_saida = item.text(14)
                db = DataBase()
                db.conecta()
                resp = db.remove_saida(codprod, data_saida)
                if resp == 'Ok':
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Saída excluida com sucesso!")
                    db.remove_geral(codprod, data_saida)
                    msg.exec()
                    self.buscar_produtos()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setWindowTitle('Erro ao excluir produto')
                    msg.setText(resp)
                    msg.exec()
                db.close_connection()

    def zerar_saidas(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Zerar Saidas")
        msg_box.setText("Você realmente deseja excluir TODAS as saidas?")

        msg_box.setStyleSheet('''
                        QPushButton {
                        background-color: rgb(0, 0, 0);
                        color: rgb(255, 255, 255);
                        }
                        QPushButton:hover {	
                        background-color: rgb(60, 60, 60);
                        }
                        QPushButton:pressed {	
                        background-color: rgb(0, 0, 0);
                        color: rgb(35, 35, 35);
                        }
                        QLabel {
                        qproperty-alignment: AlignCenter;
                        font-size: 18px;}''')

        msg_box.addButton("Sim", QMessageBox.AcceptRole)
        msg_box.addButton("Não", QMessageBox.RejectRole)

        msg_box.exec()

        if msg_box.clickedButton().text() == 'Sim':
            db = DataBase()
            db.conecta()
            db.remove_all_saida()
            db.remove_all_geral()
            db.close_connection()
            self.buscar_produtos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())
