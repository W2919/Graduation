# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(700, 900)
        Register.setStyleSheet("background-color:rgb(17,17,17)")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Register)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.unm_text = QtWidgets.QLabel(Register)
        self.unm_text.setStyleSheet("color:rgb(255, 255, 255);\n"
"border:none;\n"
"font: 10pt \"华文琥珀\";")
        self.unm_text.setObjectName("unm_text")
        self.horizontalLayout_2.addWidget(self.unm_text)
        self.unm_edit = QtWidgets.QLineEdit(Register)
        self.unm_edit.setStyleSheet("color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"华文琥珀\";")
        self.unm_edit.setObjectName("unm_edit")
        self.horizontalLayout_2.addWidget(self.unm_edit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 8)
        self.horizontalLayout_2.setStretch(2, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pwd_text = QtWidgets.QLabel(Register)
        self.pwd_text.setStyleSheet("color:rgb(255, 255, 255);\n"
"border:none;\n"
"font: 10pt \"华文琥珀\";")
        self.pwd_text.setObjectName("pwd_text")
        self.horizontalLayout_3.addWidget(self.pwd_text)
        self.pwd_edit = QtWidgets.QLineEdit(Register)
        self.pwd_edit.setStyleSheet("color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"华文琥珀\";")
        self.pwd_edit.setObjectName("pwd_edit")
        self.horizontalLayout_3.addWidget(self.pwd_edit)
        self.view_pwd_btn = QtWidgets.QPushButton(Register)
        self.view_pwd_btn.setStyleSheet("border:none")
        self.view_pwd_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/view_pwd_btn_close_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.view_pwd_btn.setIcon(icon)
        self.view_pwd_btn.setIconSize(QtCore.QSize(32, 32))
        self.view_pwd_btn.setIconSize(QtCore.QSize(32, 32))
        self.view_pwd_btn.setObjectName("view_pwd_btn")
        self.horizontalLayout_3.addWidget(self.view_pwd_btn)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 8)
        self.horizontalLayout_3.setStretch(2, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ensure_pwd_text = QtWidgets.QLabel(Register)
        self.ensure_pwd_text.setStyleSheet("color:rgb(255, 255, 255);\n"
"border:none;\n"
"font: 10pt \"华文琥珀\";")
        self.ensure_pwd_text.setObjectName("ensure_pwd_text")
        self.horizontalLayout_5.addWidget(self.ensure_pwd_text)
        self.ensure_pwd_edit = QtWidgets.QLineEdit(Register)
        self.ensure_pwd_edit.setStyleSheet("color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"华文琥珀\";")
        self.ensure_pwd_edit.setObjectName("ensure_pwd_edit")
        self.horizontalLayout_5.addWidget(self.ensure_pwd_edit)
        self.view_ensurepwd_btn = QtWidgets.QPushButton(Register)
        self.view_ensurepwd_btn.setStyleSheet("border:none\n"
"")
        self.view_ensurepwd_btn.setText("")
        self.view_ensurepwd_btn.setIcon(icon)
        self.view_ensurepwd_btn.setObjectName("view_ensurepwd_btn")
        self.view_ensurepwd_btn.setIconSize(QtCore.QSize(32, 32))
        self.horizontalLayout_5.addWidget(self.view_ensurepwd_btn)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 8)
        self.horizontalLayout_5.setStretch(2, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.phone_lbl = QtWidgets.QLabel(Register)
        self.phone_lbl.setStyleSheet("color:rgb(255, 255, 255);\n"
"border:none;\n"
"font: 10pt \"华文琥珀\";")
        self.phone_lbl.setObjectName("phone_lbl")
        self.horizontalLayout.addWidget(self.phone_lbl)
        self.phone_edit = QtWidgets.QLineEdit(Register)
        self.phone_edit.setStyleSheet("color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"华文琥珀\";")
        self.phone_edit.setObjectName("phone_edit")
        self.horizontalLayout.addWidget(self.phone_edit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 8)
        self.horizontalLayout.setStretch(2, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verifyCode_lbl = QtWidgets.QLabel(Register)
        self.verifyCode_lbl.setStyleSheet("color:rgb(255, 255, 255);\n"
"border:none;\n"
"font: 10pt \"华文琥珀\";")
        self.verifyCode_lbl.setObjectName("verifyCode_lbl")
        self.horizontalLayout_6.addWidget(self.verifyCode_lbl)
        self.verifyCode_edit = QtWidgets.QLineEdit(Register)
        self.verifyCode_edit.setStyleSheet("color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"华文琥珀\";")
        self.verifyCode_edit.setObjectName("verifyCode_edit")
        self.horizontalLayout_6.addWidget(self.verifyCode_edit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 8)
        self.horizontalLayout_6.setStretch(2, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.SMS_lbl = QtWidgets.QLabel(Register)
        self.SMS_lbl.setStyleSheet("color:rgb(255, 255, 255);\n"
"border:none;\n"
"font: 10pt \"华文琥珀\";")
        self.SMS_lbl.setObjectName("SMS_lbl")
        self.horizontalLayout_7.addWidget(self.SMS_lbl)
        self.SMS_edit = QtWidgets.QLineEdit(Register)
        self.SMS_edit.setStyleSheet("color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"华文琥珀\";")
        self.SMS_edit.setObjectName("SMS_edit")
        self.horizontalLayout_7.addWidget(self.SMS_edit)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.code_send_btn = QtWidgets.QPushButton(Register)
        self.code_send_btn.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(57,57,57);\n"
"font: 10pt \"华文琥珀\";")
        self.code_send_btn.setObjectName("code_send_btn")
        self.horizontalLayout_7.addWidget(self.code_send_btn)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 5)
        self.horizontalLayout_7.setStretch(3, 2)
        self.horizontalLayout_7.setStretch(4, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.ensure_btn = QtWidgets.QPushButton(Register)
        self.ensure_btn.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(57,57,57);\n"
"font: 10pt \"华文琥珀\";")
        self.ensure_btn.setObjectName("ensure_btn")
        self.horizontalLayout_4.addWidget(self.ensure_btn)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.return_btn = QtWidgets.QPushButton(Register)
        self.return_btn.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(57,57,57);\n"
"font: 10pt \"华文琥珀\";")
        self.return_btn.setObjectName("return_btn")
        self.horizontalLayout_4.addWidget(self.return_btn)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.setStretch(5, 1)
        self.verticalLayout_2.setStretch(6, 1)

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "Form"))
        self.unm_text.setText(_translate("Register", "用户名    ：   "))
        self.pwd_text.setText(_translate("Register", "密码      ：     "))
        self.ensure_pwd_text.setText(_translate("Register", "确认密码  ： "))
        self.phone_lbl.setText(_translate("Register", "手机号     :     "))
        self.verifyCode_lbl.setText(_translate("Register", "验证码    ：   "))
        self.SMS_lbl.setText(_translate("Register", "短信验证码："))
        self.code_send_btn.setText(_translate("Register", "发送短信验证码"))
        self.ensure_btn.setText(_translate("Register", "确认"))
        self.return_btn.setText(_translate("Register", "返回"))
