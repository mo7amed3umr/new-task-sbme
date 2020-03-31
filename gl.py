# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gl.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Glwidget = QtWidgets.QTabWidget(self.centralwidget)
        self.Glwidget.setObjectName("Glwidget")
        self.Gl_tap = QtWidgets.QWidget()
        self.Gl_tap.setObjectName("Gl_tap")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Gl_tap)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.GL_frame = QtWidgets.QFrame(self.Gl_tap)
        self.GL_frame.setObjectName("GL_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.GL_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.GL_frame)
        self.openGLWidget.setObjectName("openGLWidget")
        self.gridLayout.addWidget(self.openGLWidget, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.GL_frame, 0, 0, 1, 1)
        self.Glwidget.addTab(self.Gl_tap, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.Glwidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.Glwidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Glwidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Glwidget.setTabText(self.Glwidget.indexOf(self.Gl_tap), _translate("MainWindow", "Tab 1"))
        self.Glwidget.setTabText(self.Glwidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
