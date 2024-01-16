# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tela_Principal_2.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QFormLayout, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(903, 548)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 0, 4, 4)
        self.btn_home = QPushButton(self.centralwidget)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"\n"
"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	 color:black\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_tables = QPushButton(self.centralwidget)
        self.btn_tables.setObjectName(u"btn_tables")
        self.btn_tables.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_tables.setStyleSheet(u"\n"
"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	 color:black\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.btn_tables)

        self.btn_sobre = QPushButton(self.centralwidget)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sobre.setStyleSheet(u"\n"
"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	 color:black\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.btn_sobre)

        self.btn_contato = QPushButton(self.centralwidget)
        self.btn_contato.setObjectName(u"btn_contato")
        self.btn_contato.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_contato.setStyleSheet(u"\n"
"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	 color:black\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.btn_contato)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setEnabled(True)
        self.Pages.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pg_table = QWidget()
        self.pg_table.setObjectName(u"pg_table")
        self.verticalLayout_11 = QVBoxLayout(self.pg_table)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.tabWidget = QTabWidget(self.pg_table)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.tabWidget.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.tables = QWidget()
        self.tables.setObjectName(u"tables")
        self.gridLayout_2 = QGridLayout(self.tables)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tw_estoque = QVBoxLayout()
        self.tw_estoque.setObjectName(u"tw_estoque")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.line_busca = QLineEdit(self.tables)
        self.line_busca.setObjectName(u"line_busca")
        self.line_busca.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.line_busca)

        self.horizontalLayout_2.setStretch(0, 1)

        self.tw_estoque.addLayout(self.horizontalLayout_2)

        self.label_3 = QLabel(self.tables)
        self.label_3.setObjectName(u"label_3")

        self.tw_estoque.addWidget(self.label_3)

        self.tree_estoque = QTreeWidget(self.tables)
        self.tree_estoque.setObjectName(u"tree_estoque")
        self.tree_estoque.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.tree_estoque.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.tree_estoque.setTextElideMode(Qt.ElideLeft)

        self.tw_estoque.addWidget(self.tree_estoque)


        self.gridLayout_2.addLayout(self.tw_estoque, 0, 0, 5, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 0, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 45, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 2, 1, 1)

        self.btn_gerarsaida = QPushButton(self.tables)
        self.btn_gerarsaida.setObjectName(u"btn_gerarsaida")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_gerarsaida.sizePolicy().hasHeightForWidth())
        self.btn_gerarsaida.setSizePolicy(sizePolicy)
        self.btn_gerarsaida.setMinimumSize(QSize(120, 28))
        self.btn_gerarsaida.setMaximumSize(QSize(120, 28))
        self.btn_gerarsaida.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gerarsaida.setLayoutDirection(Qt.LeftToRight)
        self.btn_gerarsaida.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 11pt \"MS Shell Dlg 2\";	\n"
"	border-radius:10px\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(85, 255, 127);\n"
"	 color:black\n"
"}\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"imagens/Certo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_gerarsaida.setIcon(icon)
        self.btn_gerarsaida.setIconSize(QSize(20, 20))
#if QT_CONFIG(shortcut)
        self.btn_gerarsaida.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.gridLayout_2.addWidget(self.btn_gerarsaida, 2, 2, 1, 1)

        self.btn_excluirmerc = QPushButton(self.tables)
        self.btn_excluirmerc.setObjectName(u"btn_excluirmerc")
        sizePolicy.setHeightForWidth(self.btn_excluirmerc.sizePolicy().hasHeightForWidth())
        self.btn_excluirmerc.setSizePolicy(sizePolicy)
        self.btn_excluirmerc.setMinimumSize(QSize(120, 28))
        self.btn_excluirmerc.setMaximumSize(QSize(120, 28))
        self.btn_excluirmerc.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluirmerc.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 10.5pt \"MS Shell Dlg 2\";	\n"
"	border-radius:10px\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(255, 61, 61);\n"
"	 color:black\n"
"}\n"
"\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"imagens/X.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_excluirmerc.setIcon(icon1)
        self.btn_excluirmerc.setIconSize(QSize(18, 18))
        self.btn_excluirmerc.setFlat(False)

        self.gridLayout_2.addWidget(self.btn_excluirmerc, 3, 2, 1, 1)

        self.btn_editaritem = QPushButton(self.tables)
        self.btn_editaritem.setObjectName(u"btn_editaritem")
        self.btn_editaritem.setMinimumSize(QSize(120, 28))
        self.btn_editaritem.setMaximumSize(QSize(120, 28))
        self.btn_editaritem.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_editaritem.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 11pt \"MS Shell Dlg 2\";	\n"
"	border-radius:10px\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	background-color: rgb(255, 122, 55);\n"
"	 color:black\n"
"}\n"
"\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"imagens/editar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_editaritem.setIcon(icon2)
        self.btn_editaritem.setIconSize(QSize(17, 17))

        self.gridLayout_2.addWidget(self.btn_editaritem, 1, 2, 1, 1)

        self.tw_saida = QVBoxLayout()
        self.tw_saida.setObjectName(u"tw_saida")
        self.label = QLabel(self.tables)
        self.label.setObjectName(u"label")

        self.tw_saida.addWidget(self.label)

        self.tree_saida = QTreeWidget(self.tables)
        self.tree_saida.setObjectName(u"tree_saida")
        self.tree_saida.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))

        self.tw_saida.addWidget(self.tree_saida)


        self.gridLayout_2.addLayout(self.tw_saida, 5, 0, 1, 1)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, -1, -1, -1)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_7, 4, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_4, 0, 0, 1, 1)

        self.btn_gerarestorno = QPushButton(self.tables)
        self.btn_gerarestorno.setObjectName(u"btn_gerarestorno")
        self.btn_gerarestorno.setMinimumSize(QSize(120, 28))
        self.btn_gerarestorno.setMaximumSize(QSize(120, 28))
        self.btn_gerarestorno.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gerarestorno.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 11pt \"MS Shell Dlg 2\";	\n"
"	border-radius:10px\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"	 color:black\n"
"}\n"
"\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"imagens/Estorno.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_gerarestorno.setIcon(icon3)
        self.btn_gerarestorno.setIconSize(QSize(20, 23))

        self.gridLayout_13.addWidget(self.btn_gerarestorno, 1, 0, 1, 1)

        self.btn_zerarsaidas = QPushButton(self.tables)
        self.btn_zerarsaidas.setObjectName(u"btn_zerarsaidas")
        self.btn_zerarsaidas.setMinimumSize(QSize(120, 28))
        self.btn_zerarsaidas.setMaximumSize(QSize(120, 28))
        self.btn_zerarsaidas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_zerarsaidas.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 11pt \"MS Shell Dlg 2\";	\n"
"	border-radius:10px\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 85, 127);\n"
"	 color:black\n"
"}\n"
"\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"imagens/zerar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_zerarsaidas.setIcon(icon4)
        self.btn_zerarsaidas.setIconSize(QSize(24, 22))

        self.gridLayout_13.addWidget(self.btn_zerarsaidas, 3, 0, 1, 1)

        self.btn_excluirsaida = QPushButton(self.tables)
        self.btn_excluirsaida.setObjectName(u"btn_excluirsaida")
        self.btn_excluirsaida.setMinimumSize(QSize(120, 28))
        self.btn_excluirsaida.setMaximumSize(QSize(120, 28))
        self.btn_excluirsaida.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluirsaida.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 11pt \"MS Shell Dlg 2\";	\n"
"	border-radius:10px\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(255, 61, 61);\n"
"	 color:black\n"
"}\n"
"\n"
"\n"
"")
        self.btn_excluirsaida.setIcon(icon1)
        self.btn_excluirsaida.setIconSize(QSize(18, 18))

        self.gridLayout_13.addWidget(self.btn_excluirsaida, 2, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_13, 5, 2, 1, 1)

        self.tabWidget.addTab(self.tables, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(6)
        self.gridLayout_4.setContentsMargins(-1, -1, 9, -1)
        self.txt_search = QLineEdit(self.tab_2)
        self.txt_search.setObjectName(u"txt_search")
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.txt_search.setFont(font)
        self.txt_search.setStyleSheet(u"\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.txt_search.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.txt_search, 5, 4, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, 0, -1)
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_15)

        self.label_29 = QLabel(self.tab_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.label_29)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_16)


        self.gridLayout_4.addLayout(self.horizontalLayout_3, 6, 4, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.btn_gerargrafico = QPushButton(self.tab_2)
        self.btn_gerargrafico.setObjectName(u"btn_gerargrafico")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_gerargrafico.sizePolicy().hasHeightForWidth())
        self.btn_gerargrafico.setSizePolicy(sizePolicy1)
        self.btn_gerargrafico.setMinimumSize(QSize(120, 28))
        self.btn_gerargrafico.setMaximumSize(QSize(120, 28))
        self.btn_gerargrafico.setSizeIncrement(QSize(0, 0))
        self.btn_gerargrafico.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gerargrafico.setStyleSheet(u"\n"
"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	font: 75 12pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:10px\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(85, 170, 255);\n"
"	 color:black;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_9.addWidget(self.btn_gerargrafico)

        self.btn_gerarexcel = QPushButton(self.tab_2)
        self.btn_gerarexcel.setObjectName(u"btn_gerarexcel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_gerarexcel.sizePolicy().hasHeightForWidth())
        self.btn_gerarexcel.setSizePolicy(sizePolicy2)
        self.btn_gerarexcel.setMinimumSize(QSize(120, 28))
        self.btn_gerarexcel.setMaximumSize(QSize(120, 28))
        self.btn_gerarexcel.setSizeIncrement(QSize(0, 0))
        self.btn_gerarexcel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gerarexcel.setStyleSheet(u"\n"
"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	font: 75 12pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:10px\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(85, 255, 127);\n"
"	 color:black;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_9.addWidget(self.btn_gerarexcel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)


        self.gridLayout_4.addLayout(self.horizontalLayout_9, 0, 4, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.tree_geral = QTreeWidget(self.tab_2)
        self.tree_geral.setObjectName(u"tree_geral")
        self.tree_geral.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))

        self.horizontalLayout_4.addWidget(self.tree_geral)


        self.gridLayout_4.addLayout(self.horizontalLayout_4, 7, 4, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_17)

        self.btn_removertopofila = QPushButton(self.tab_2)
        self.btn_removertopofila.setObjectName(u"btn_removertopofila")
        self.btn_removertopofila.setMinimumSize(QSize(170, 28))
        self.btn_removertopofila.setMaximumSize(QSize(170, 28))
        self.btn_removertopofila.setStyleSheet(u"\n"
"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	font: 75 12pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:10px\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 75, 75);\n"
"	 color:black;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.btn_removertopofila)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_18)


        self.gridLayout_4.addLayout(self.horizontalLayout_6, 8, 4, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_3 = QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(6)
        self.label_13 = QLabel(self.tab_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_13, 7, 0, 1, 1)

        self.line_emitente = QLineEdit(self.tab_3)
        self.line_emitente.setObjectName(u"line_emitente")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.line_emitente.sizePolicy().hasHeightForWidth())
        self.line_emitente.setSizePolicy(sizePolicy3)
        self.line_emitente.setMinimumSize(QSize(0, 20))
        self.line_emitente.setMaximumSize(QSize(16777215, 20))
        self.line_emitente.setSizeIncrement(QSize(0, 0))
        self.line_emitente.setInputMethodHints(Qt.ImhNone)
        self.line_emitente.setClearButtonEnabled(False)

        self.gridLayout_3.addWidget(self.line_emitente, 6, 0, 1, 1)

        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setMaximumSize(QSize(16777215, 30))
        self.label_8.setFocusPolicy(Qt.NoFocus)
        self.label_8.setLayoutDirection(Qt.LeftToRight)
        self.label_8.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_8, 1, 4, 1, 1)

        self.line_descprod = QLineEdit(self.tab_3)
        self.line_descprod.setObjectName(u"line_descprod")

        self.gridLayout_3.addWidget(self.line_descprod, 6, 2, 1, 1)

        self.line_preco = QLineEdit(self.tab_3)
        self.line_preco.setObjectName(u"line_preco")

        self.gridLayout_3.addWidget(self.line_preco, 8, 0, 1, 1)

        self.label_6 = QLabel(self.tab_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_6, 5, 4, 1, 1)

        self.label_11 = QLabel(self.tab_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 30))
        self.label_11.setMaximumSize(QSize(16777215, 30))
        self.label_11.setFocusPolicy(Qt.NoFocus)
        self.label_11.setLayoutDirection(Qt.LeftToRight)
        self.label_11.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_11, 5, 0, 1, 1)

        self.line_cnpjemitente = QLineEdit(self.tab_3)
        self.line_cnpjemitente.setObjectName(u"line_cnpjemitente")
        sizePolicy3.setHeightForWidth(self.line_cnpjemitente.sizePolicy().hasHeightForWidth())
        self.line_cnpjemitente.setSizePolicy(sizePolicy3)
        self.line_cnpjemitente.setMinimumSize(QSize(0, 20))
        self.line_cnpjemitente.setMaximumSize(QSize(16777215, 20))
        self.line_cnpjemitente.setMaxLength(14)

        self.gridLayout_3.addWidget(self.line_cnpjemitente, 4, 4, 1, 1)

        self.label_7 = QLabel(self.tab_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 30))
        self.label_7.setMaximumSize(QSize(16777215, 30))
        self.label_7.setFocusPolicy(Qt.NoFocus)
        self.label_7.setLayoutDirection(Qt.LeftToRight)
        self.label_7.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_7, 1, 2, 1, 1)

        self.label_14 = QLabel(self.tab_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 30))
        self.label_14.setMaximumSize(QSize(16777215, 30))
        self.label_14.setFocusPolicy(Qt.NoFocus)
        self.label_14.setLayoutDirection(Qt.LeftToRight)
        self.label_14.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_14, 3, 0, 1, 1)

        self.line_chavedeacessonfe = QLineEdit(self.tab_3)
        self.line_chavedeacessonfe.setObjectName(u"line_chavedeacessonfe")
        sizePolicy3.setHeightForWidth(self.line_chavedeacessonfe.sizePolicy().hasHeightForWidth())
        self.line_chavedeacessonfe.setSizePolicy(sizePolicy3)
        self.line_chavedeacessonfe.setMinimumSize(QSize(0, 20))
        self.line_chavedeacessonfe.setMaximumSize(QSize(16777215, 20))
        self.line_chavedeacessonfe.setMaxLength(40)

        self.gridLayout_3.addWidget(self.line_chavedeacessonfe, 4, 2, 1, 1)

        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 30))
        self.label_2.setFocusPolicy(Qt.NoFocus)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.line_nfe = QLineEdit(self.tab_3)
        self.line_nfe.setObjectName(u"line_nfe")
        sizePolicy3.setHeightForWidth(self.line_nfe.sizePolicy().hasHeightForWidth())
        self.line_nfe.setSizePolicy(sizePolicy3)
        self.line_nfe.setMinimumSize(QSize(0, 20))
        self.line_nfe.setMaximumSize(QSize(16777215, 20))
        self.line_nfe.setMaxLength(9)

        self.gridLayout_3.addWidget(self.line_nfe, 2, 2, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(-1, -1, 8, -1)
        self.label_5 = QLabel(self.tab_3)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMinimumSize(QSize(360, 40))
        self.label_5.setMaximumSize(QSize(360, 40))
        self.label_5.setStyleSheet(u"font: 75 26pt \"MS Shell Dlg 2\";")

        self.gridLayout_8.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_28 = QLabel(self.tab_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(40, 40))
        self.label_28.setMaximumSize(QSize(40, 40))
        self.label_28.setPixmap(QPixmap(u"imagens/mercadorias.png"))
        self.label_28.setScaledContents(True)

        self.gridLayout_8.addWidget(self.label_28, 0, 2, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_8, 0, 2, 1, 1)

        self.line_codprod = QLineEdit(self.tab_3)
        self.line_codprod.setObjectName(u"line_codprod")
        sizePolicy3.setHeightForWidth(self.line_codprod.sizePolicy().hasHeightForWidth())
        self.line_codprod.setSizePolicy(sizePolicy3)
        self.line_codprod.setMinimumSize(QSize(0, 20))
        self.line_codprod.setMaximumSize(QSize(16777215, 20))
        self.line_codprod.setMaxLength(14)

        self.gridLayout_3.addWidget(self.line_codprod, 2, 0, 1, 1)

        self.line_serienfe = QLineEdit(self.tab_3)
        self.line_serienfe.setObjectName(u"line_serienfe")
        sizePolicy3.setHeightForWidth(self.line_serienfe.sizePolicy().hasHeightForWidth())
        self.line_serienfe.setSizePolicy(sizePolicy3)
        self.line_serienfe.setMinimumSize(QSize(0, 20))
        self.line_serienfe.setMaximumSize(QSize(16777215, 20))
        self.line_serienfe.setMaxLength(3)

        self.gridLayout_3.addWidget(self.line_serienfe, 2, 4, 1, 1)

        self.label_10 = QLabel(self.tab_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 30))
        self.label_10.setMaximumSize(QSize(16777215, 30))
        self.label_10.setFocusPolicy(Qt.NoFocus)
        self.label_10.setLayoutDirection(Qt.LeftToRight)
        self.label_10.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_10, 3, 4, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_14, 0, 4, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_13, 0, 0, 1, 1)

        self.label_12 = QLabel(self.tab_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 30))
        self.label_12.setMaximumSize(QSize(16777215, 30))
        self.label_12.setFocusPolicy(Qt.NoFocus)
        self.label_12.setLayoutDirection(Qt.LeftToRight)
        self.label_12.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_12, 5, 2, 1, 1)

        self.label_9 = QLabel(self.tab_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 30))
        self.label_9.setMaximumSize(QSize(16777215, 30))
        self.label_9.setFocusPolicy(Qt.NoFocus)
        self.label_9.setLayoutDirection(Qt.LeftToRight)
        self.label_9.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_9, 3, 2, 1, 1)

        self.line_unidade = QLineEdit(self.tab_3)
        self.line_unidade.setObjectName(u"line_unidade")

        self.gridLayout_3.addWidget(self.line_unidade, 6, 4, 1, 1)

        self.line_quantidade = QLineEdit(self.tab_3)
        self.line_quantidade.setObjectName(u"line_quantidade")

        self.gridLayout_3.addWidget(self.line_quantidade, 8, 2, 1, 1)

        self.label_15 = QLabel(self.tab_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_15, 7, 2, 1, 1)

        self.label_25 = QLabel(self.tab_3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_25, 9, 2, 1, 1)

        self.label_24 = QLabel(self.tab_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_24, 7, 4, 1, 1)

        self.cb_avaria = QComboBox(self.tab_3)
        self.cb_avaria.addItem("")
        self.cb_avaria.addItem("")
        self.cb_avaria.setObjectName(u"cb_avaria")
        self.cb_avaria.setMaxVisibleItems(2)

        self.gridLayout_3.addWidget(self.cb_avaria, 10, 2, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.label_40 = QLabel(self.tab_3)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_5.addWidget(self.label_40, 0, 0, 1, 1)

        self.btn_cadastrarmerc = QPushButton(self.tab_3)
        self.btn_cadastrarmerc.setObjectName(u"btn_cadastrarmerc")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_cadastrarmerc.sizePolicy().hasHeightForWidth())
        self.btn_cadastrarmerc.setSizePolicy(sizePolicy4)
        self.btn_cadastrarmerc.setMinimumSize(QSize(250, 35))
        self.btn_cadastrarmerc.setMaximumSize(QSize(250, 35))
        self.btn_cadastrarmerc.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrarmerc.setLayoutDirection(Qt.LeftToRight)
        self.btn_cadastrarmerc.setAutoFillBackground(False)
        self.btn_cadastrarmerc.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 0, 0);\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(85, 255, 127);\n"
"	 color:black\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_5.addWidget(self.btn_cadastrarmerc, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_5, 11, 2, 1, 1)

        self.date_emissaonfs = QDateEdit(self.tab_3)
        self.date_emissaonfs.setObjectName(u"date_emissaonfs")

        self.gridLayout_3.addWidget(self.date_emissaonfs, 4, 0, 1, 1)

        self.date_entradaproduto = QDateEdit(self.tab_3)
        self.date_entradaproduto.setObjectName(u"date_entradaproduto")

        self.gridLayout_3.addWidget(self.date_entradaproduto, 8, 4, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_11.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_table)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.gridLayout_6 = QGridLayout(self.pg_home)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_45 = QLabel(self.pg_home)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_6.addWidget(self.label_45, 2, 3, 1, 1)

        self.label_44 = QLabel(self.pg_home)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_6.addWidget(self.label_44, 2, 0, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_48 = QLabel(self.pg_home)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(1, 1))
        self.label_48.setMaximumSize(QSize(1, 1))

        self.gridLayout_7.addWidget(self.label_48, 7, 1, 1, 1)

        self.label_46 = QLabel(self.pg_home)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_7.addWidget(self.label_46, 5, 0, 1, 1)

        self.label_47 = QLabel(self.pg_home)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_7.addWidget(self.label_47, 5, 2, 1, 1)

        self.label_49 = QLabel(self.pg_home)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(1, 1))
        self.label_49.setMaximumSize(QSize(1, 1))

        self.gridLayout_7.addWidget(self.label_49, 2, 1, 1, 1)

        self.label_4 = QLabel(self.pg_home)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(350, 320))
        self.label_4.setMaximumSize(QSize(350, 320))
        self.label_4.setPixmap(QPixmap(u"imagens/logo_junta3.png"))
        self.label_4.setScaledContents(True)

        self.gridLayout_7.addWidget(self.label_4, 1, 1, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_cadastrarusuario = QPushButton(self.pg_home)
        self.btn_cadastrarusuario.setObjectName(u"btn_cadastrarusuario")
        sizePolicy1.setHeightForWidth(self.btn_cadastrarusuario.sizePolicy().hasHeightForWidth())
        self.btn_cadastrarusuario.setSizePolicy(sizePolicy1)
        self.btn_cadastrarusuario.setMinimumSize(QSize(220, 30))
        self.btn_cadastrarusuario.setMaximumSize(QSize(220, 30))
        self.btn_cadastrarusuario.setSizeIncrement(QSize(0, 0))
        self.btn_cadastrarusuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrarusuario.setLayoutDirection(Qt.LeftToRight)
        self.btn_cadastrarusuario.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 0, 0);\n"
"	font: 75 12pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	animation: buttonAnimation 0.5s;\n"
"}\n"
"\n"
"@keyframes buttonAnimation {\n"
"	0% { background-color: rgb(85, 170, 255); }\n"
"	50% { background-color: rgb(255, 85, 85); }\n"
"	100% { background-color: rgb(85, 170, 255); }\n"
"}\n"
"")
        self.btn_cadastrarusuario.setAutoDefault(False)
        self.btn_cadastrarusuario.setFlat(False)

        self.horizontalLayout_11.addWidget(self.btn_cadastrarusuario)


        self.gridLayout_7.addLayout(self.horizontalLayout_11, 4, 1, 1, 1)

        self.btn_sair = QPushButton(self.pg_home)
        self.btn_sair.setObjectName(u"btn_sair")
        sizePolicy1.setHeightForWidth(self.btn_sair.sizePolicy().hasHeightForWidth())
        self.btn_sair.setSizePolicy(sizePolicy1)
        self.btn_sair.setMinimumSize(QSize(370, 30))
        self.btn_sair.setMaximumSize(QSize(370, 30))
        self.btn_sair.setStyleSheet(u"\n"
"QPushButton{\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius:10px\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	 color:black;\n"
"color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.btn_sair.setAutoDefault(False)
        self.btn_sair.setFlat(False)

        self.gridLayout_7.addWidget(self.btn_sair, 5, 1, 1, 1)

        self.label_18 = QLabel(self.pg_home)
        self.label_18.setObjectName(u"label_18")
        sizePolicy1.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy1)
        self.label_18.setMinimumSize(QSize(0, 10))
        self.label_18.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_7.addWidget(self.label_18, 3, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 42, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_8, 0, 1, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_9, 6, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_7, 2, 1, 1, 2)

        self.Pages.addWidget(self.pg_home)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.formLayout_7 = QFormLayout(self.pg_cadastro)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setHorizontalSpacing(0)
        self.formLayout_7.setVerticalSpacing(12)
        self.formLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(-1, 0, 0, -1)
        self.formLayout_9 = QFormLayout()
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.formLayout_9.setHorizontalSpacing(0)
        self.formLayout_9.setVerticalSpacing(0)
        self.formLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.pg_cadastro)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(280, 45))
        self.label_16.setMaximumSize(QSize(280, 45))
        self.label_16.setStyleSheet(u"font: 75 26pt \"MS Shell Dlg 2\";")

        self.formLayout_9.setWidget(0, QFormLayout.LabelRole, self.label_16)

        self.label_17 = QLabel(self.pg_cadastro)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(40, 40))
        self.label_17.setMaximumSize(QSize(40, 40))
        self.label_17.setPixmap(QPixmap(u"imagens/usuario.png"))
        self.label_17.setScaledContents(True)

        self.formLayout_9.setWidget(0, QFormLayout.FieldRole, self.label_17)


        self.gridLayout_14.addLayout(self.formLayout_9, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)


        self.formLayout_7.setLayout(0, QFormLayout.FieldRole, self.gridLayout_14)

        self.verticalSpacer_6 = QSpacerItem(20, 91, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_7.setItem(4, QFormLayout.FieldRole, self.verticalSpacer_6)

        self.label_52 = QLabel(self.pg_cadastro)
        self.label_52.setObjectName(u"label_52")

        self.formLayout_7.setWidget(5, QFormLayout.FieldRole, self.label_52)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setHorizontalSpacing(5)
        self.gridLayout_16.setVerticalSpacing(13)
        self.gridLayout_16.setContentsMargins(0, 0, -1, -1)
        self.label_20 = QLabel(self.pg_cadastro)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFocusPolicy(Qt.NoFocus)
        self.label_20.setLayoutDirection(Qt.LeftToRight)
        self.label_20.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_20, 1, 0, 1, 1)

        self.cad_usuario = QLineEdit(self.pg_cadastro)
        self.cad_usuario.setObjectName(u"cad_usuario")
        sizePolicy3.setHeightForWidth(self.cad_usuario.sizePolicy().hasHeightForWidth())
        self.cad_usuario.setSizePolicy(sizePolicy3)

        self.gridLayout_16.addWidget(self.cad_usuario, 1, 1, 1, 1)

        self.label_19 = QLabel(self.pg_cadastro)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFocusPolicy(Qt.NoFocus)
        self.label_19.setLayoutDirection(Qt.LeftToRight)
        self.label_19.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_19, 0, 0, 1, 1)

        self.cad_nome = QLineEdit(self.pg_cadastro)
        self.cad_nome.setObjectName(u"cad_nome")
        sizePolicy3.setHeightForWidth(self.cad_nome.sizePolicy().hasHeightForWidth())
        self.cad_nome.setSizePolicy(sizePolicy3)
        self.cad_nome.setMinimumSize(QSize(320, 20))
        self.cad_nome.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_16.addWidget(self.cad_nome, 0, 1, 1, 1)

        self.cad_senha = QLineEdit(self.pg_cadastro)
        self.cad_senha.setObjectName(u"cad_senha")
        sizePolicy3.setHeightForWidth(self.cad_senha.sizePolicy().hasHeightForWidth())
        self.cad_senha.setSizePolicy(sizePolicy3)
        self.cad_senha.setMaximumSize(QSize(16777215, 20))
        self.cad_senha.setEchoMode(QLineEdit.Password)
        self.cad_senha.setClearButtonEnabled(False)

        self.gridLayout_16.addWidget(self.cad_senha, 2, 1, 1, 1)

        self.label_22 = QLabel(self.pg_cadastro)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFocusPolicy(Qt.NoFocus)
        self.label_22.setLayoutDirection(Qt.LeftToRight)
        self.label_22.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_22, 3, 0, 1, 1)

        self.cb_perfil = QComboBox(self.pg_cadastro)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        sizePolicy1.setHeightForWidth(self.cb_perfil.sizePolicy().hasHeightForWidth())
        self.cb_perfil.setSizePolicy(sizePolicy1)
        self.cb_perfil.setMinimumSize(QSize(110, 20))
        self.cb_perfil.setMaximumSize(QSize(110, 20))
        self.cb_perfil.setBaseSize(QSize(0, 0))
        self.cb_perfil.setLayoutDirection(Qt.LeftToRight)
        self.cb_perfil.setAutoFillBackground(False)
        self.cb_perfil.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"")

        self.gridLayout_16.addWidget(self.cb_perfil, 4, 1, 1, 1)

        self.label_21 = QLabel(self.pg_cadastro)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFocusPolicy(Qt.NoFocus)
        self.label_21.setLayoutDirection(Qt.LeftToRight)
        self.label_21.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_21, 2, 0, 1, 1)

        self.cad_confirmarsenha = QLineEdit(self.pg_cadastro)
        self.cad_confirmarsenha.setObjectName(u"cad_confirmarsenha")
        sizePolicy3.setHeightForWidth(self.cad_confirmarsenha.sizePolicy().hasHeightForWidth())
        self.cad_confirmarsenha.setSizePolicy(sizePolicy3)
        self.cad_confirmarsenha.setEchoMode(QLineEdit.Password)

        self.gridLayout_16.addWidget(self.cad_confirmarsenha, 3, 1, 1, 1)

        self.label_23 = QLabel(self.pg_cadastro)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFocusPolicy(Qt.NoFocus)
        self.label_23.setLayoutDirection(Qt.RightToLeft)
        self.label_23.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_23, 4, 0, 1, 1)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, -1, -1)
        self.verticalSpacer_5 = QSpacerItem(0, 4, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.cad_btncadastro = QPushButton(self.pg_cadastro)
        self.cad_btncadastro.setObjectName(u"cad_btncadastro")
        sizePolicy1.setHeightForWidth(self.cad_btncadastro.sizePolicy().hasHeightForWidth())
        self.cad_btncadastro.setSizePolicy(sizePolicy1)
        self.cad_btncadastro.setMinimumSize(QSize(250, 30))
        self.cad_btncadastro.setMaximumSize(QSize(250, 30))
        self.cad_btncadastro.setCursor(QCursor(Qt.PointingHandCursor))
        self.cad_btncadastro.setLayoutDirection(Qt.LeftToRight)
        self.cad_btncadastro.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(85, 255, 127);\n"
"	 color:black\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_15.addWidget(self.cad_btncadastro, 1, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_8, 1, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_7, 1, 0, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_15, 5, 0, 1, 2)


        self.formLayout_7.setLayout(1, QFormLayout.FieldRole, self.gridLayout_16)

        self.Pages.addWidget(self.pg_cadastro)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_10 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(0)
        self.gridLayout_9.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, -1)
        self.label_76 = QLabel(self.pg_sobre)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setStyleSheet(u"font: 75 26pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_5.addWidget(self.label_76)

        self.label_75 = QLabel(self.pg_sobre)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMinimumSize(QSize(40, 46))
        self.label_75.setMaximumSize(QSize(40, 46))
        self.label_75.setPixmap(QPixmap(u"imagens/sobre.png"))
        self.label_75.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_75)


        self.gridLayout_9.addLayout(self.horizontalLayout_5, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_6, 0, 2, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_9)

        self.label_72 = QLabel(self.pg_sobre)
        self.label_72.setObjectName(u"label_72")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_72.sizePolicy().hasHeightForWidth())
        self.label_72.setSizePolicy(sizePolicy5)
        self.label_72.setMinimumSize(QSize(0, 0))
        self.label_72.setStyleSheet(u"")
        self.label_72.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.label_72)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_13)

        self.Pages.addWidget(self.pg_sobre)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        self.formLayout_3 = QFormLayout(self.pg_contato)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(0)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_9, 0, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_10, 0, 4, 1, 1)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, 0, -1, -1)
        self.label_26 = QLabel(self.pg_contato)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(140, 40))
        self.label_26.setMaximumSize(QSize(140, 40))

        self.horizontalLayout_24.addWidget(self.label_26)

        self.label_27 = QLabel(self.pg_contato)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(40, 40))
        self.label_27.setMaximumSize(QSize(40, 40))
        self.label_27.setPixmap(QPixmap(u"imagens/contato.png"))
        self.label_27.setScaledContents(True)

        self.horizontalLayout_24.addWidget(self.label_27)


        self.gridLayout_10.addLayout(self.horizontalLayout_24, 0, 2, 1, 1)


        self.formLayout_3.setLayout(1, QFormLayout.FieldRole, self.gridLayout_10)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(8, 8, 8, 8)
        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setHorizontalSpacing(13)
        self.formLayout_6.setVerticalSpacing(27)
        self.formLayout_6.setContentsMargins(-1, 10, 10, -1)
        self.label_35 = QLabel(self.pg_contato)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(40, 40))
        self.label_35.setMaximumSize(QSize(40, 40))
        self.label_35.setPixmap(QPixmap(u"imagens/telefone.png"))
        self.label_35.setScaledContents(True)

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_35)

        self.label_36 = QLabel(self.pg_contato)
        self.label_36.setObjectName(u"label_36")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.label_36)

        self.label_37 = QLabel(self.pg_contato)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(40, 40))
        self.label_37.setMaximumSize(QSize(40, 40))
        self.label_37.setPixmap(QPixmap(u"imagens/telefone.png"))
        self.label_37.setScaledContents(True)

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_37)

        self.label_71 = QLabel(self.pg_contato)
        self.label_71.setObjectName(u"label_71")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.label_71)

        self.label_73 = QLabel(self.pg_contato)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setMinimumSize(QSize(40, 40))
        self.label_73.setMaximumSize(QSize(40, 40))
        self.label_73.setSizeIncrement(QSize(0, 0))
        self.label_73.setPixmap(QPixmap(u"imagens/whatsapp.png"))
        self.label_73.setScaledContents(True)

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.label_73)

        self.label_74 = QLabel(self.pg_contato)
        self.label_74.setObjectName(u"label_74")

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.label_74)

        self.label_77 = QLabel(self.pg_contato)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setMinimumSize(QSize(40, 40))
        self.label_77.setMaximumSize(QSize(40, 40))
        self.label_77.setPixmap(QPixmap(u"imagens/instagram.png"))
        self.label_77.setScaledContents(True)

        self.formLayout_6.setWidget(3, QFormLayout.LabelRole, self.label_77)

        self.label_78 = QLabel(self.pg_contato)
        self.label_78.setObjectName(u"label_78")

        self.formLayout_6.setWidget(3, QFormLayout.FieldRole, self.label_78)

        self.label_79 = QLabel(self.pg_contato)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setMinimumSize(QSize(40, 40))
        self.label_79.setMaximumSize(QSize(40, 40))
        self.label_79.setPixmap(QPixmap(u"imagens/facebook.png"))
        self.label_79.setScaledContents(True)

        self.formLayout_6.setWidget(4, QFormLayout.LabelRole, self.label_79)

        self.label_82 = QLabel(self.pg_contato)
        self.label_82.setObjectName(u"label_82")

        self.formLayout_6.setWidget(4, QFormLayout.FieldRole, self.label_82)

        self.label_83 = QLabel(self.pg_contato)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setMinimumSize(QSize(40, 40))
        self.label_83.setMaximumSize(QSize(40, 40))
        self.label_83.setPixmap(QPixmap(u"imagens/twitter.png"))
        self.label_83.setScaledContents(True)

        self.formLayout_6.setWidget(5, QFormLayout.LabelRole, self.label_83)

        self.label_84 = QLabel(self.pg_contato)
        self.label_84.setObjectName(u"label_84")

        self.formLayout_6.setWidget(5, QFormLayout.FieldRole, self.label_84)


        self.gridLayout_11.addLayout(self.formLayout_6, 0, 1, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_12, 0, 2, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_11, 0, 0, 1, 1)


        self.formLayout_3.setLayout(2, QFormLayout.FieldRole, self.gridLayout_11)

        self.Pages.addWidget(self.pg_contato)

        self.gridLayout.addWidget(self.Pages, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        self.cb_avaria.setCurrentIndex(-1)
        self.btn_cadastrarusuario.setDefault(False)
        self.btn_sair.setDefault(False)
        self.cb_perfil.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_tables.setText(QCoreApplication.translate("MainWindow", u"TABELAS", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"CONTATO", None))
        self.line_busca.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Busca...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">ESTOQUE</span></p></body></html>", None))
        ___qtreewidgetitem = self.tree_estoque.headerItem()
        ___qtreewidgetitem.setText(13, QCoreApplication.translate("MainWindow", u"Avaria", None));
        ___qtreewidgetitem.setText(12, QCoreApplication.translate("MainWindow", u"Data Entrada", None));
        ___qtreewidgetitem.setText(11, QCoreApplication.translate("MainWindow", u"Total", None));
        ___qtreewidgetitem.setText(10, QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtreewidgetitem.setText(9, QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None));
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("MainWindow", u"Unidade", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Emitente", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Cnpj Emitente", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Chave de Acesso", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Data de Emiss\u00e3o (NF-e)", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"S\u00e9rie", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"NF-e", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"C\u00f3digo do Produto", None));
        self.btn_gerarsaida.setText(QCoreApplication.translate("MainWindow", u"Gerar Sa\u00edda", None))
        self.btn_excluirmerc.setText(QCoreApplication.translate("MainWindow", u"Excluir Prod.", None))
        self.btn_editaritem.setText(QCoreApplication.translate("MainWindow", u"Editar Item", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">SA\u00cdDA</span></p></body></html>", None))
        ___qtreewidgetitem1 = self.tree_saida.headerItem()
        ___qtreewidgetitem1.setText(14, QCoreApplication.translate("MainWindow", u"Data Sa\u00edda", None));
        ___qtreewidgetitem1.setText(13, QCoreApplication.translate("MainWindow", u"Avaria", None));
        ___qtreewidgetitem1.setText(12, QCoreApplication.translate("MainWindow", u"Data Entrada", None));
        ___qtreewidgetitem1.setText(11, QCoreApplication.translate("MainWindow", u"Total", None));
        ___qtreewidgetitem1.setText(10, QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtreewidgetitem1.setText(9, QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None));
        ___qtreewidgetitem1.setText(8, QCoreApplication.translate("MainWindow", u"Unidade", None));
        ___qtreewidgetitem1.setText(7, QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtreewidgetitem1.setText(6, QCoreApplication.translate("MainWindow", u"Emitente", None));
        ___qtreewidgetitem1.setText(5, QCoreApplication.translate("MainWindow", u"Cnpj Emitente", None));
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"Chave de Acesso", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"Data de Emiss\u00e3o (NF-e)", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"S\u00e9rie", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"NF-e", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"C\u00f3digo do Produto", None));
        self.btn_gerarestorno.setText(QCoreApplication.translate("MainWindow", u"Gerar Estorno", None))
        self.btn_zerarsaidas.setText(QCoreApplication.translate("MainWindow", u"Zerar Saidas", None))
        self.btn_excluirsaida.setText(QCoreApplication.translate("MainWindow", u"Excluir Saida", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tables), QCoreApplication.translate("MainWindow", u"Gerenciamento de Estoque", None))
        self.txt_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Busca...", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">FILA DE SA\u00cdDAS</span></p></body></html>", None))
        self.btn_gerargrafico.setText(QCoreApplication.translate("MainWindow", u"Gerar Gr\u00e1fico", None))
        self.btn_gerarexcel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        ___qtreewidgetitem2 = self.tree_geral.headerItem()
        ___qtreewidgetitem2.setText(15, QCoreApplication.translate("MainWindow", u"Data Saida", None));
        ___qtreewidgetitem2.setText(14, QCoreApplication.translate("MainWindow", u"Avaria", None));
        ___qtreewidgetitem2.setText(13, QCoreApplication.translate("MainWindow", u"Data Entrada", None));
        ___qtreewidgetitem2.setText(12, QCoreApplication.translate("MainWindow", u"Total", None));
        ___qtreewidgetitem2.setText(11, QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtreewidgetitem2.setText(10, QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None));
        ___qtreewidgetitem2.setText(9, QCoreApplication.translate("MainWindow", u"Unidade", None));
        ___qtreewidgetitem2.setText(8, QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtreewidgetitem2.setText(7, QCoreApplication.translate("MainWindow", u"Emitente", None));
        ___qtreewidgetitem2.setText(6, QCoreApplication.translate("MainWindow", u"Cnpj Emitente", None));
        ___qtreewidgetitem2.setText(5, QCoreApplication.translate("MainWindow", u"Chave de Acesso", None));
        ___qtreewidgetitem2.setText(4, QCoreApplication.translate("MainWindow", u"Data de Emiss\u00e3o (NF-e)", None));
        ___qtreewidgetitem2.setText(3, QCoreApplication.translate("MainWindow", u"S\u00e9rie", None));
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("MainWindow", u"NF-e", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"C\u00f3digo do Produto", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"N\u00ba", None));
        self.btn_removertopofila.setText(QCoreApplication.translate("MainWindow", u"Remover N\u00ba1 (Fila)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"An\u00e1lise de Estoque e Saida", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None))
#if QT_CONFIG(accessibility)
        self.line_emitente.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.line_emitente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: Miriade", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"S\u00e9rie (NF-e)", None))
        self.line_descprod.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: Cal\u00e7a Jeans", None))
        self.line_preco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: 119,99", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Unidade", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Emitente (NF-e)", None))
#if QT_CONFIG(accessibility)
        self.line_cnpjemitente.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.line_cnpjemitente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: 54353611000142", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"NF-e", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Data de Emiss\u00e3o (NF-e)", None))
#if QT_CONFIG(accessibility)
        self.line_chavedeacessonfe.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.line_chavedeacessonfe.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: 3249182759819287654562134567891827465324", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo do Produto", None))
#if QT_CONFIG(accessibility)
        self.line_nfe.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.line_nfe.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: 412876918", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">Cadastro de Mercadorias</span></p></body></html>", None))
        self.label_28.setText("")
#if QT_CONFIG(accessibility)
        self.line_codprod.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.line_codprod.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: 12201234598723", None))
#if QT_CONFIG(accessibility)
        self.line_serienfe.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.line_serienfe.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: 020 ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"CNPJ Emitente (NF-e)", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Chave de Acesso (NF-e)", None))
        self.line_unidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: CX", None))
        self.line_quantidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: 20", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Avaria", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Data de Entrada (Produto)", None))
        self.cb_avaria.setItemText(0, QCoreApplication.translate("MainWindow", u"Sim", None))
        self.cb_avaria.setItemText(1, QCoreApplication.translate("MainWindow", u"N\u00e3o", None))

        self.label_40.setText("")
        self.btn_cadastrarmerc.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Mercadoria", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Cadastro de Mercadorias", None))
        self.label_45.setText("")
        self.label_44.setText("")
        self.label_48.setText("")
        self.label_46.setText("")
        self.label_47.setText("")
        self.label_49.setText("")
        self.label_4.setText("")
        self.btn_cadastrarusuario.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.btn_sair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.label_18.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Tela de Cadastro</span></p></body></html>", None))
        self.label_17.setText("")
        self.label_52.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio:", None))
#if QT_CONFIG(accessibility)
        self.cad_usuario.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.cad_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: Warleson.Rocha", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
#if QT_CONFIG(accessibility)
        self.cad_nome.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.cad_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: Warleson da Rocha de Sousa", None))
#if QT_CONFIG(accessibility)
        self.cad_senha.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.cad_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: 2093kdol", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Confirme a senha:", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
#if QT_CONFIG(accessibility)
        self.cad_confirmarsenha.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.cad_confirmarsenha.setPlaceholderText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Perfil:", None))
        self.cad_btncadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Sobre</span></p></body></html>", None))
        self.label_75.setText("")
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Bem-vindo ao </span><span style=\" font-size:11pt; font-weight:600; text-decoration: underline;\">PyStock</span><span style=\" font-size:11pt;\"> - seu parceiro de gerenciamento de estoque eficiente!</span></p><p align=\"justify\"><span style=\" font-size:11pt; color:#ffffff;\">aaaaaaa</span><span style=\" font-size:11pt;\">O </span><span style=\" font-size:11pt; font-weight:600;\">PyStock</span><span style=\" font-size:11pt;\"> \u00e9 um poderoso programa de </span><span style=\" font-size:11pt; font-weight:600;\">gerenciamento de estoque</span><span style=\" font-size:11pt;\"> desenvolvido para ajudar sua empresa a otimizar o controle de produtos e materiais. Com nossa solu\u00e7\u00e3o completa e intuitiva, voc\u00ea poder\u00e1 evitar desperd\u00edcios, reduzir custos e oferecer um servi\u00e7o de qualidade excepcional aos seus clientes.<br/></span><span style=\" font-size:11pt; color:#ffffff;\">aaaaaaa</span><span style=\" font-size:1"
                        "1pt;\">Nossa ferramenta foi desenvolvida em Python, utilizando a biblioteca PySide6 e o software QtDesign para fornecer uma interface gr\u00e1fica amig\u00e1vel e de f\u00e1cil utiliza\u00e7\u00e3o. Com recursos avan\u00e7ados e personaliz\u00e1veis, o PyStock atende \u00e0s necessidades espec\u00edficas de sua empresa, seja ela uma transportadora, varejista ou qualquer outro setor que necessite de um controle de estoque eficiente.</span></p><p align=\"justify\"><span style=\" font-size:11pt; font-weight:600;\">Destaques do PyStock</span><span style=\" font-size:11pt;\">:</span></p><p align=\"justify\"><span style=\" font-size:11pt;\">- </span><span style=\" font-size:11pt; font-weight:600;\">Gerenciamento de estoque abrangente</span><span style=\" font-size:11pt;\">: Controle e rastreie seus produtos e materiais com precis\u00e3o, desde a entrada at\u00e9 a sa\u00edda, mantendo um invent\u00e1rio atualizado e confi\u00e1vel.</span></p><p align=\"justify\"><span style=\" font-size:11pt;\">- </span><span style="
                        "\" font-size:11pt; font-weight:600;\">Integra\u00e7\u00e3o com banco de dados SqlLite: </span><span style=\" font-size:11pt;\">Armazene todas as informa\u00e7\u00f5es de estoque e gerenciamento em um local seguro e confi\u00e1vel, garantindo f\u00e1cil acesso e backup dos dados.</span></p><p align=\"justify\"><span style=\" font-size:11pt;\">- </span><span style=\" font-size:11pt; font-weight:600;\">Contas de administradores e usu\u00e1rios: </span><span style=\" font-size:11pt;\">Diferencie as permiss\u00f5es no sistema de acordo com o n\u00edvel de acesso de cada usu\u00e1rio, garantindo a seguran\u00e7a e confidencialidade dos dados.</span></p><p align=\"justify\"><span style=\" font-size:11pt; font-weight:600;\">- Gera\u00e7\u00e3o de Gr\u00e1ficos e Planilhas Excel:</span><span style=\" font-size:11pt;\"> Al\u00e9m dos recursos mencionados anteriormente, o PyStock oferece uma funcionalidade de gera\u00e7\u00e3o de gr\u00e1fico e planilhas Excel. Com essa capacidade integrada, voc\u00ea poder\u00e1 visuali"
                        "zar facilmente dados de estoque em forma de gr\u00e1ficos informativos e exportar informa\u00e7\u00f5es essenciais para planilhas Excel.</span></p><p align=\"justify\"><span style=\" font-size:11pt;\"><br/></span></p><p align=\"center\"><span style=\" font-size:11pt;\"><br/></span></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:26pt; font-weight:600;\">Contato</span></p></body></html>", None))
        self.label_27.setText("")
        self.label_35.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">(91)98937-2407</span></p></body></html>", None))
        self.label_37.setText("")
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">(91)98548-6893</span></p></body></html>", None))
        self.label_73.setText("")
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">(91)98548-6893</span></p></body></html>", None))
        self.label_77.setText("")
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">@PyStock</span></p></body></html>", None))
        self.label_79.setText("")
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">pystock.app</span></p></body></html>", None))
        self.label_83.setText("")
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">@PyStock</span></p></body></html>", None))
    # retranslateUi

