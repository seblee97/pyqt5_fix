# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './designerFiles/loader_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoadPointDialog(object):
    def setupUi(self, LoadPointDialog):
        LoadPointDialog.setObjectName("LoadPointDialog")
        LoadPointDialog.resize(388, 276)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(LoadPointDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(LoadPointDialog)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.FileListTextEdit = QtWidgets.QTextEdit(LoadPointDialog)
        self.FileListTextEdit.setObjectName("FileListTextEdit")
        self.horizontalLayout_2.addWidget(self.FileListTextEdit)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.loadToolButton = QtWidgets.QToolButton(LoadPointDialog)
        self.loadToolButton.setObjectName("loadToolButton")
        self.verticalLayout.addWidget(self.loadToolButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(LoadPointDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.XYDoubleSpinBox = QtWidgets.QDoubleSpinBox(LoadPointDialog)
        self.XYDoubleSpinBox.setDecimals(3)
        self.XYDoubleSpinBox.setSingleStep(0.1)
        self.XYDoubleSpinBox.setProperty("value", 1.0)
        self.XYDoubleSpinBox.setObjectName("XYDoubleSpinBox")
        self.horizontalLayout.addWidget(self.XYDoubleSpinBox)
        self.label_3 = QtWidgets.QLabel(LoadPointDialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.ZDoubleSpinBox = QtWidgets.QDoubleSpinBox(LoadPointDialog)
        self.ZDoubleSpinBox.setDecimals(3)
        self.ZDoubleSpinBox.setSingleStep(0.1)
        self.ZDoubleSpinBox.setProperty("value", 1.0)
        self.ZDoubleSpinBox.setObjectName("ZDoubleSpinBox")
        self.horizontalLayout.addWidget(self.ZDoubleSpinBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(LoadPointDialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.FirstSliceSpinBox = QtWidgets.QSpinBox(LoadPointDialog)
        self.FirstSliceSpinBox.setMinimum(0)
        self.FirstSliceSpinBox.setMaximum(9999)
        self.FirstSliceSpinBox.setObjectName("FirstSliceSpinBox")
        self.horizontalLayout_4.addWidget(self.FirstSliceSpinBox)
        self.label_5 = QtWidgets.QLabel(LoadPointDialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.LastSliceSpinBox = QtWidgets.QSpinBox(LoadPointDialog)
        self.LastSliceSpinBox.setMinimum(-1)
        self.LastSliceSpinBox.setMaximum(9999)
        self.LastSliceSpinBox.setProperty("value", -1)
        self.LastSliceSpinBox.setObjectName("LastSliceSpinBox")
        self.horizontalLayout_4.addWidget(self.LastSliceSpinBox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.buttonBox = QtWidgets.QDialogButtonBox(LoadPointDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.label.setBuddy(self.FileListTextEdit)
        self.label_2.setBuddy(self.XYDoubleSpinBox)
        self.label_3.setBuddy(self.ZDoubleSpinBox)
        self.label_4.setBuddy(self.FirstSliceSpinBox)
        self.label_5.setBuddy(self.LastSliceSpinBox)

        self.retranslateUi(LoadPointDialog)
        self.buttonBox.accepted.connect(LoadPointDialog.accept)
        self.buttonBox.rejected.connect(LoadPointDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LoadPointDialog)
        LoadPointDialog.setTabOrder(self.FileListTextEdit, self.loadToolButton)
        LoadPointDialog.setTabOrder(self.loadToolButton, self.XYDoubleSpinBox)
        LoadPointDialog.setTabOrder(self.XYDoubleSpinBox, self.ZDoubleSpinBox)
        LoadPointDialog.setTabOrder(self.ZDoubleSpinBox, self.FirstSliceSpinBox)
        LoadPointDialog.setTabOrder(self.FirstSliceSpinBox, self.LastSliceSpinBox)

    def retranslateUi(self, LoadPointDialog):
        _translate = QtCore.QCoreApplication.translate
        LoadPointDialog.setWindowTitle(_translate("LoadPointDialog", "Dialog"))
        self.label.setText(_translate("LoadPointDialog", "File &list"))
        self.FileListTextEdit.setToolTip(_translate("LoadPointDialog", "List of file to load. "))
        self.loadToolButton.setText(_translate("LoadPointDialog", "..."))
        self.label_2.setText(_translate("LoadPointDialog", "&x/y scale:"))
        self.label_3.setText(_translate("LoadPointDialog", "&z scale:"))
        self.label_4.setText(_translate("LoadPointDialog", "&First slice:"))
        self.label_5.setText(_translate("LoadPointDialog", "&Last slice:"))

