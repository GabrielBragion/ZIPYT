# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSlider,
    QWidget)

class Ui_Window(object):
    def setupUi(self, Window):
        if not Window.objectName():
            Window.setObjectName(u"Window")
        Window.setEnabled(True)
        Window.resize(290, 450)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Window.sizePolicy().hasHeightForWidth())
        Window.setSizePolicy(sizePolicy)
        Window.setMinimumSize(QSize(290, 450))
        Window.setMaximumSize(QSize(290, 450))
        font = QFont()
        font.setBold(True)
        Window.setFont(font)
        Window.setAcceptDrops(True)
        self.label_files = QLabel(Window)
        self.label_files.setObjectName(u"label_files")
        self.label_files.setGeometry(QRect(9, 9, 124, 16))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_files.sizePolicy().hasHeightForWidth())
        self.label_files.setSizePolicy(sizePolicy1)
        self.input_files = QLineEdit(Window)
        self.input_files.setObjectName(u"input_files")
        self.input_files.setGeometry(QRect(10, 30, 191, 30))
        self.input_files.setMinimumSize(QSize(0, 30))
        self.input_files.setMaximumSize(QSize(16777215, 30))
        self.btn_load = QPushButton(Window)
        self.btn_load.setObjectName(u"btn_load")
        self.btn_load.setGeometry(QRect(210, 30, 75, 30))
        self.btn_load.setMinimumSize(QSize(0, 30))
        self.btn_load.setMaximumSize(QSize(16777215, 30))
        self.btn_load.setFont(font)
        self.btn_load.setAutoFillBackground(False)
        self.btn_load.setStyleSheet(u"QPushButton {\n"
"    background-color: #0B3642;   /* Azul ZYPit */\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"")
        self.label_method = QLabel(Window)
        self.label_method.setObjectName(u"label_method")
        self.label_method.setGeometry(QRect(10, 110, 115, 30))
        self.label_method.setMinimumSize(QSize(0, 30))
        self.label_method.setMaximumSize(QSize(16777215, 30))
        self.slider_level = QSlider(Window)
        self.slider_level.setObjectName(u"slider_level")
        self.slider_level.setGeometry(QRect(10, 220, 271, 30))
        self.slider_level.setMinimumSize(QSize(0, 30))
        self.slider_level.setMaximumSize(QSize(16777215, 30))
        self.slider_level.setMinimum(1)
        self.slider_level.setMaximum(9)
        self.slider_level.setOrientation(Qt.Orientation.Horizontal)
        self.slider_level.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider_level.setTickInterval(1)
        self.select_method = QComboBox(Window)
        self.select_method.addItem("")
        self.select_method.addItem("")
        self.select_method.addItem("")
        self.select_method.addItem("")
        self.select_method.setObjectName(u"select_method")
        self.select_method.setGeometry(QRect(210, 110, 71, 30))
        self.select_method.setMinimumSize(QSize(0, 30))
        self.select_method.setMaximumSize(QSize(16777215, 30))
        self.select_compress = QComboBox(Window)
        self.select_compress.addItem("")
        self.select_compress.addItem("")
        self.select_compress.addItem("")
        self.select_compress.addItem("")
        self.select_compress.addItem("")
        self.select_compress.setObjectName(u"select_compress")
        self.select_compress.setGeometry(QRect(200, 150, 85, 30))
        self.select_compress.setMinimumSize(QSize(0, 30))
        self.select_compress.setMaximumSize(QSize(16777215, 30))
        self.label_compress = QLabel(Window)
        self.label_compress.setObjectName(u"label_compress")
        self.label_compress.setGeometry(QRect(10, 150, 181, 30))
        self.label_compress.setMinimumSize(QSize(0, 30))
        self.label_compress.setMaximumSize(QSize(16777215, 30))
        self.label_level = QLabel(Window)
        self.label_level.setObjectName(u"label_level")
        self.label_level.setGeometry(QRect(10, 190, 120, 30))
        self.label_level.setMinimumSize(QSize(0, 30))
        self.label_level.setMaximumSize(QSize(16777215, 30))
        self.layoutWidget = QWidget(Window)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 250, 271, 30))
        self.layoutWidget.setMinimumSize(QSize(0, 30))
        self.layoutWidget.setMaximumSize(QSize(16777215, 30))
        self.label_numbers = QHBoxLayout(self.layoutWidget)
        self.label_numbers.setSpacing(18)
        self.label_numbers.setObjectName(u"label_numbers")
        self.label_numbers.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 30))
        self.label_5.setMaximumSize(QSize(16777215, 30))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_numbers.addWidget(self.label_5)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 30))
        self.label_9.setMaximumSize(QSize(16777215, 30))
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_numbers.addWidget(self.label_9)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setMaximumSize(QSize(16777215, 30))
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_numbers.addWidget(self.label_8)

        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 30))
        self.label_12.setMaximumSize(QSize(16777215, 30))
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_numbers.addWidget(self.label_12)

        self.label_13 = QLabel(self.layoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 30))
        self.label_13.setMaximumSize(QSize(16777215, 30))
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_numbers.addWidget(self.label_13)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 30))
        self.label_10.setMaximumSize(QSize(16777215, 30))
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_numbers.addWidget(self.label_10)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 30))
        self.label_11.setMaximumSize(QSize(16777215, 30))
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_numbers.addWidget(self.label_11)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 30))
        self.label_7.setMaximumSize(QSize(16777215, 30))
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_numbers.addWidget(self.label_7)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 30))
        self.label_6.setMaximumSize(QSize(16777215, 30))
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_numbers.addWidget(self.label_6)

        self.input_password = QLineEdit(Window)
        self.input_password.setObjectName(u"input_password")
        self.input_password.setGeometry(QRect(100, 290, 181, 30))
        self.input_password.setMinimumSize(QSize(0, 30))
        self.input_password.setMaximumSize(QSize(16777215, 30))
        self.input_password.setMaxLength(32)
        self.input_password.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.label_password = QLabel(Window)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setGeometry(QRect(10, 290, 80, 30))
        self.label_password.setMinimumSize(QSize(0, 30))
        self.label_password.setMaximumSize(QSize(16777215, 30))
        self.btn_exec = QPushButton(Window)
        self.btn_exec.setObjectName(u"btn_exec")
        self.btn_exec.setGeometry(QRect(10, 410, 271, 30))
        self.btn_exec.setMinimumSize(QSize(0, 30))
        self.btn_exec.setMaximumSize(QSize(16777215, 30))
        self.btn_exec.setStyleSheet(u"QPushButton {\n"
"    background-color: #0B3642;   /* Azul ZYPit */\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"")
        self.label_repeat = QLabel(Window)
        self.label_repeat.setObjectName(u"label_repeat")
        self.label_repeat.setGeometry(QRect(10, 330, 40, 30))
        self.label_repeat.setMinimumSize(QSize(0, 30))
        self.label_repeat.setMaximumSize(QSize(16777215, 30))
        self.checkbox_delete = QCheckBox(Window)
        self.checkbox_delete.setObjectName(u"checkbox_delete")
        self.checkbox_delete.setGeometry(QRect(10, 370, 166, 30))
        self.checkbox_delete.setMinimumSize(QSize(0, 30))
        self.checkbox_delete.setMaximumSize(QSize(16777215, 30))
        self.input_repeat = QLineEdit(Window)
        self.input_repeat.setObjectName(u"input_repeat")
        self.input_repeat.setGeometry(QRect(100, 330, 181, 30))
        self.input_repeat.setMinimumSize(QSize(0, 30))
        self.input_repeat.setMaximumSize(QSize(16777215, 30))
        self.input_repeat.setMaxLength(32)
        self.input_repeat.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.drag_and_drop = QFrame(Window)
        self.drag_and_drop.setObjectName(u"drag_and_drop")
        self.drag_and_drop.setEnabled(False)
        self.drag_and_drop.setGeometry(QRect(0, 0, 291, 451))
        self.drag_and_drop.setAcceptDrops(True)
        self.drag_and_drop.setAutoFillBackground(False)
        self.drag_and_drop.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.5);  /* Transpar\u00eancia */\n"
"border: 2px dashed #00BFFF;           /* Borda tracejada azul */")
        self.drag_and_drop.setFrameShape(QFrame.Shape.StyledPanel)
        self.drag_and_drop.setFrameShadow(QFrame.Shadow.Raised)
        self.label_drag_and_drop = QLabel(self.drag_and_drop)
        self.label_drag_and_drop.setObjectName(u"label_drag_and_drop")
        self.label_drag_and_drop.setGeometry(QRect(30, 200, 231, 31))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_drag_and_drop.setFont(font1)
        self.label_drag_and_drop.setStyleSheet(u"border: none;")
        self.label_drag_and_drop.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.list_files = QListWidget(Window)
        self.list_files.setObjectName(u"list_files")
        self.list_files.setGeometry(QRect(10, 70, 271, 30))
        self.list_files.setMinimumSize(QSize(0, 30))
        self.list_files.setMaximumSize(QSize(16777215, 30))
        self.label_files.raise_()
        self.input_files.raise_()
        self.btn_load.raise_()
        self.label_method.raise_()
        self.slider_level.raise_()
        self.select_method.raise_()
        self.select_compress.raise_()
        self.label_compress.raise_()
        self.label_level.raise_()
        self.layoutWidget.raise_()
        self.input_password.raise_()
        self.label_password.raise_()
        self.btn_exec.raise_()
        self.label_repeat.raise_()
        self.checkbox_delete.raise_()
        self.input_repeat.raise_()
        self.list_files.raise_()
        self.drag_and_drop.raise_()

        self.retranslateUi(Window)

        QMetaObject.connectSlotsByName(Window)
    # setupUi

    def retranslateUi(self, Window):
        Window.setWindowTitle(QCoreApplication.translate("Window", u"ZIPYT", None))
        self.label_files.setText(QCoreApplication.translate("Window", u"Selecione os arquivos:", None))
        self.btn_load.setText(QCoreApplication.translate("Window", u"&Carregar", None))
        self.label_method.setText(QCoreApplication.translate("Window", u"Selecione o metodo:", None))
        self.select_method.setItemText(0, QCoreApplication.translate("Window", u"TAR", None))
        self.select_method.setItemText(1, QCoreApplication.translate("Window", u"ZIP", None))
        self.select_method.setItemText(2, QCoreApplication.translate("Window", u"GZ", None))
        self.select_method.setItemText(3, QCoreApplication.translate("Window", u"LZMA", None))

        self.select_compress.setItemText(0, QCoreApplication.translate("Window", u"Nenhum", None))
        self.select_compress.setItemText(1, QCoreApplication.translate("Window", u"Padr\u00e3o", None))
        self.select_compress.setItemText(2, QCoreApplication.translate("Window", u"BZIP2", None))
        self.select_compress.setItemText(3, QCoreApplication.translate("Window", u"GZIP", None))
        self.select_compress.setItemText(4, QCoreApplication.translate("Window", u"LZMA", None))

        self.label_compress.setText(QCoreApplication.translate("Window", u"Selecione o tipo de compress\u00e3o:", None))
        self.label_level.setText(QCoreApplication.translate("Window", u"Nivel de compress\u00e3o:", None))
        self.label_5.setText(QCoreApplication.translate("Window", u"1", None))
        self.label_9.setText(QCoreApplication.translate("Window", u"2", None))
        self.label_8.setText(QCoreApplication.translate("Window", u"3", None))
        self.label_12.setText(QCoreApplication.translate("Window", u"4", None))
        self.label_13.setText(QCoreApplication.translate("Window", u"5", None))
        self.label_10.setText(QCoreApplication.translate("Window", u"6", None))
        self.label_11.setText(QCoreApplication.translate("Window", u"7", None))
        self.label_7.setText(QCoreApplication.translate("Window", u"8", None))
        self.label_6.setText(QCoreApplication.translate("Window", u"9", None))
        self.label_password.setText(QCoreApplication.translate("Window", u"Palavra-Passe:", None))
        self.btn_exec.setText(QCoreApplication.translate("Window", u"&Executar", None))
        self.label_repeat.setText(QCoreApplication.translate("Window", u"Repita:", None))
        self.checkbox_delete.setText(QCoreApplication.translate("Window", u"Deletar arquivo original?", None))
        self.label_drag_and_drop.setText(QCoreApplication.translate("Window", u"Solte o arquivo aqui", None))
    # retranslateUi

