# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modifyUser.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(674, 437)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.modify_pwd_lbl = QtWidgets.QLabel(Form)
        self.modify_pwd_lbl.setObjectName("modify_pwd_lbl")
        self.horizontalLayout.addWidget(self.modify_pwd_lbl)
        self.modify_pwd_edit = QtWidgets.QLineEdit(Form)
        self.modify_pwd_edit.setObjectName("modify_pwd_edit")
        self.horizontalLayout.addWidget(self.modify_pwd_edit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 15)
        self.horizontalLayout.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.modify_newpwd_lbl = QtWidgets.QLabel(Form)
        self.modify_newpwd_lbl.setObjectName("modify_newpwd_lbl")
        self.horizontalLayout_2.addWidget(self.modify_newpwd_lbl)
        self.modify_newpwd_edit = QtWidgets.QLineEdit(Form)
        self.modify_newpwd_edit.setObjectName("modify_newpwd_edit")
        self.horizontalLayout_2.addWidget(self.modify_newpwd_edit)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 5)
        self.horizontalLayout_2.setStretch(2, 15)
        self.horizontalLayout_2.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.modify_ensure_newpwd_lbl = QtWidgets.QLabel(Form)
        self.modify_ensure_newpwd_lbl.setObjectName("modify_ensure_newpwd_lbl")
        self.horizontalLayout_4.addWidget(self.modify_ensure_newpwd_lbl)
        self.modify_ensure_newpwd_edit = QtWidgets.QLineEdit(Form)
        self.modify_ensure_newpwd_edit.setObjectName("modify_ensure_newpwd_edit")
        self.horizontalLayout_4.addWidget(self.modify_ensure_newpwd_edit)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 5)
        self.horizontalLayout_4.setStretch(2, 15)
        self.horizontalLayout_4.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.ensureModifyButton = QtWidgets.QPushButton(Form)
        self.ensureModifyButton.setObjectName("ensureModifyButton")
        self.horizontalLayout_3.addWidget(self.ensureModifyButton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.returnButton = QtWidgets.QPushButton(Form)
        self.returnButton.setObjectName("returnButton")
        self.horizontalLayout_3.addWidget(self.returnButton)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.modify_pwd_lbl.setText(_translate("Form", "原密码："))
        self.modify_newpwd_lbl.setText(_translate("Form", "新密码："))
        self.modify_ensure_newpwd_lbl.setText(_translate("Form", "确认新密码："))
        self.ensureModifyButton.setText(_translate("Form", "确定"))
        self.returnButton.setText(_translate("Form", "返回"))
