# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BrainLabelingGui_v15.ui'
#
# Created: Mon Aug 29 13:43:38 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_BrainLabelingGui(object):
    def setupUi(self, BrainLabelingGui):
        BrainLabelingGui.setObjectName(_fromUtf8("BrainLabelingGui"))
        BrainLabelingGui.resize(1521, 1113)
        self.centralwidget = QtGui.QWidget(BrainLabelingGui)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.splitter_3 = QtGui.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.sagittal_gview = QtGui.QGraphicsView(self.splitter_3)
        self.sagittal_gview.setObjectName(_fromUtf8("sagittal_gview"))
        self.splitter_2 = QtGui.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.coronal_gview = QtGui.QGraphicsView(self.splitter)
        self.coronal_gview.setObjectName(_fromUtf8("coronal_gview"))
        self.horizontal_gview = QtGui.QGraphicsView(self.splitter)
        self.horizontal_gview.setObjectName(_fromUtf8("horizontal_gview"))
        self.layoutWidget = QtGui.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.slider_hxy = QtGui.QSlider(self.layoutWidget)
        self.slider_hxy.setMinimum(-100)
        self.slider_hxy.setMaximum(100)
        self.slider_hxy.setTracking(True)
        self.slider_hxy.setOrientation(QtCore.Qt.Horizontal)
        self.slider_hxy.setInvertedAppearance(False)
        self.slider_hxy.setInvertedControls(False)
        self.slider_hxy.setTickPosition(QtGui.QSlider.TicksAbove)
        self.slider_hxy.setObjectName(_fromUtf8("slider_hxy"))
        self.gridLayout.addWidget(self.slider_hxy, 1, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1)
        self.slider_hxz = QtGui.QSlider(self.layoutWidget)
        self.slider_hxz.setMinimum(-100)
        self.slider_hxz.setMaximum(100)
        self.slider_hxz.setOrientation(QtCore.Qt.Horizontal)
        self.slider_hxz.setObjectName(_fromUtf8("slider_hxz"))
        self.gridLayout.addWidget(self.slider_hxz, 1, 4, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.slider_hyx = QtGui.QSlider(self.layoutWidget)
        self.slider_hyx.setMinimum(-100)
        self.slider_hyx.setMaximum(100)
        self.slider_hyx.setOrientation(QtCore.Qt.Horizontal)
        self.slider_hyx.setObjectName(_fromUtf8("slider_hyx"))
        self.gridLayout.addWidget(self.slider_hyx, 2, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 3, 1, 1)
        self.slider_hyz = QtGui.QSlider(self.layoutWidget)
        self.slider_hyz.setMinimum(-100)
        self.slider_hyz.setMaximum(100)
        self.slider_hyz.setOrientation(QtCore.Qt.Horizontal)
        self.slider_hyz.setObjectName(_fromUtf8("slider_hyz"))
        self.gridLayout.addWidget(self.slider_hyz, 2, 4, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)
        self.slider_hzx = QtGui.QSlider(self.layoutWidget)
        self.slider_hzx.setMinimum(-100)
        self.slider_hzx.setMaximum(100)
        self.slider_hzx.setOrientation(QtCore.Qt.Horizontal)
        self.slider_hzx.setObjectName(_fromUtf8("slider_hzx"))
        self.gridLayout.addWidget(self.slider_hzx, 3, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 3, 3, 1, 1)
        self.slider_hzy = QtGui.QSlider(self.layoutWidget)
        self.slider_hzy.setMinimum(-100)
        self.slider_hzy.setMaximum(100)
        self.slider_hzy.setOrientation(QtCore.Qt.Horizontal)
        self.slider_hzy.setObjectName(_fromUtf8("slider_hzy"))
        self.gridLayout.addWidget(self.slider_hzy, 3, 4, 1, 1)
        self.button_symmetric = QtGui.QPushButton(self.layoutWidget)
        self.button_symmetric.setObjectName(_fromUtf8("button_symmetric"))
        self.gridLayout.addWidget(self.button_symmetric, 1, 5, 1, 1)
        self.button_displayStructures = QtGui.QPushButton(self.layoutWidget)
        self.button_displayStructures.setObjectName(_fromUtf8("button_displayStructures"))
        self.gridLayout.addWidget(self.button_displayStructures, 1, 6, 1, 1)
        self.button_displayOptions = QtGui.QPushButton(self.layoutWidget)
        self.button_displayOptions.setObjectName(_fromUtf8("button_displayOptions"))
        self.gridLayout.addWidget(self.button_displayOptions, 2, 5, 1, 1)
        self.button_inferSide = QtGui.QPushButton(self.layoutWidget)
        self.button_inferSide.setObjectName(_fromUtf8("button_inferSide"))
        self.gridLayout.addWidget(self.button_inferSide, 2, 6, 1, 1)
        self.button_save = QtGui.QPushButton(self.layoutWidget)
        self.button_save.setObjectName(_fromUtf8("button_save"))
        self.gridLayout.addWidget(self.button_save, 3, 5, 1, 1)
        self.button_load = QtGui.QPushButton(self.layoutWidget)
        self.button_load.setObjectName(_fromUtf8("button_load"))
        self.gridLayout.addWidget(self.button_load, 3, 6, 1, 1)
        self.lineEdit_username = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_username.setObjectName(_fromUtf8("lineEdit_username"))
        self.gridLayout.addWidget(self.lineEdit_username, 4, 6, 1, 1)
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 4, 5, 1, 1)
        self.button_stop = QtGui.QPushButton(self.layoutWidget)
        self.button_stop.setObjectName(_fromUtf8("button_stop"))
        self.gridLayout.addWidget(self.button_stop, 4, 4, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 4, 1, 1)
        self.gridLayout_2.addWidget(self.splitter_3, 0, 0, 1, 1)
        BrainLabelingGui.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(BrainLabelingGui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1521, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        BrainLabelingGui.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(BrainLabelingGui)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        BrainLabelingGui.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(BrainLabelingGui)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        BrainLabelingGui.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(BrainLabelingGui)
        QtCore.QMetaObject.connectSlotsByName(BrainLabelingGui)

    def retranslateUi(self, BrainLabelingGui):
        BrainLabelingGui.setWindowTitle(_translate("BrainLabelingGui", "MainWindow", None))
        self.label.setText(_translate("BrainLabelingGui", "h_xy", None))
        self.label_4.setText(_translate("BrainLabelingGui", "h_xz", None))
        self.label_2.setText(_translate("BrainLabelingGui", "h_yx", None))
        self.label_5.setText(_translate("BrainLabelingGui", "h_yz", None))
        self.label_3.setText(_translate("BrainLabelingGui", "h_zx", None))
        self.label_6.setText(_translate("BrainLabelingGui", "h_zy", None))
        self.button_symmetric.setText(_translate("BrainLabelingGui", "Symmetric", None))
        self.button_displayStructures.setText(_translate("BrainLabelingGui", "Display Structures", None))
        self.button_displayOptions.setText(_translate("BrainLabelingGui", "Display Options", None))
        self.button_inferSide.setText(_translate("BrainLabelingGui", "Infer Side", None))
        self.button_save.setText(_translate("BrainLabelingGui", "Save", None))
        self.button_load.setText(_translate("BrainLabelingGui", "Load", None))
        self.label_7.setText(_translate("BrainLabelingGui", "Username:", None))
        self.button_stop.setText(_translate("BrainLabelingGui", "Stop Loading", None))
        self.toolBar.setWindowTitle(_translate("BrainLabelingGui", "toolBar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    BrainLabelingGui = QtGui.QMainWindow()
    ui = Ui_BrainLabelingGui()
    ui.setupUi(BrainLabelingGui)
    BrainLabelingGui.show()
    sys.exit(app.exec_())

