# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tela_Login2.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Tela_Login(object):
    def setupUi(self, Tela_Login):
        if not Tela_Login.objectName():
            Tela_Login.setObjectName(u"Tela_Login")
        Tela_Login.setWindowModality(Qt.NonModal)
        Tela_Login.resize(388, 403)
        Tela_Login.setLayoutDirection(Qt.RightToLeft)
        Tela_Login.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Login = QWidget(Tela_Login)
        self.Login.setObjectName(u"Login")
        self.Login.setLayoutDirection(Qt.RightToLeft)
        self.Login.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(self.Login)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.Login)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.frame = QFrame(self.Login)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(300, 500))
        self.frame.setLayoutDirection(Qt.RightToLeft)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(1)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.logo_nome = QLabel(self.frame)
        self.logo_nome.setObjectName(u"logo_nome")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logo_nome.sizePolicy().hasHeightForWidth())
        self.logo_nome.setSizePolicy(sizePolicy1)
        self.logo_nome.setMaximumSize(QSize(210, 210))
        self.logo_nome.setPixmap(QPixmap(u"imagens/logo_junta3.png"))
        self.logo_nome.setScaledContents(True)
        self.logo_nome.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.logo_nome, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_6)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, 0, 0, 0)
        self.txt_password = QLineEdit(self.frame)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setMinimumSize(QSize(200, 33))
        self.txt_password.setMaximumSize(QSize(200, 33))
        self.txt_password.setFocusPolicy(Qt.ClickFocus)
        self.txt_password.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(45, 45, 45);\n"
"	border-radius: 5px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid;\n"
"	color: rgb(0, 0, 0);	\n"
"}")
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.txt_password, 4, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_5, 4, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 5, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_6, 4, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.txt_user = QLineEdit(self.frame)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setMinimumSize(QSize(0, 33))
        self.txt_user.setMaximumSize(QSize(200, 33))
        self.txt_user.setFocusPolicy(Qt.ClickFocus)
        self.txt_user.setLayoutDirection(Qt.RightToLeft)
        self.txt_user.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(45, 45, 45);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid;\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.txt_user.setMaxLength(32767)
        self.txt_user.setFrame(True)
        self.txt_user.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.txt_user, 1, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_5)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(-1, 0, 0, 0)
        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy2)
        self.btn_login.setMinimumSize(QSize(150, 35))
        self.btn_login.setMaximumSize(QSize(150, 35))
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setLayoutDirection(Qt.RightToLeft)
        self.btn_login.setStyleSheet(u"\n"
"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:10px;\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	border: 2px solid;\n"
"	background-color: rgb(40, 170, 255);\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	 color:black\n"
"}\n"
"\n"
"\n"
"")
        self.btn_login.setIconSize(QSize(16, 16))

        self.gridLayout_7.addWidget(self.btn_login, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_3, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_7)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.verticalLayout.addLayout(self.gridLayout_2)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.label_2 = QLabel(self.Login)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        Tela_Login.setCentralWidget(self.Login)

        self.retranslateUi(Tela_Login)

        QMetaObject.connectSlotsByName(Tela_Login)
    # setupUi

    def retranslateUi(self, Tela_Login):
        Tela_Login.setWindowTitle(QCoreApplication.translate("Tela_Login", u"MainWindow", None))
        self.label.setText("")
        self.logo_nome.setText("")
        self.txt_password.setPlaceholderText(QCoreApplication.translate("Tela_Login", u"password", None))
        self.txt_user.setPlaceholderText(QCoreApplication.translate("Tela_Login", u"user", None))
        self.btn_login.setText(QCoreApplication.translate("Tela_Login", u"Login", None))
        self.label_2.setText("")
    # retranslateUi

