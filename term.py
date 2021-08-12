#import of modules
from PyQt5 import QtCore, QtGui, QtWidgets
import os,sys

#Creating UiClass
class Ui_Terminal(object):
    def setupUi(self, Terminal):
        Terminal.setObjectName("Terminal")
        Terminal.resize(817, 545)
        Terminal.setSizeIncrement(QtCore.QSize(5, 5))

        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)

        Terminal.setFont(font)
        Terminal.setMouseTracking(True)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("terminal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Terminal.setWindowIcon(icon)

        self.scrollArea = QtWidgets.QScrollArea(Terminal)
        self.scrollArea.setGeometry(QtCore.QRect(10, 70, 781, 451))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 779, 449))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Droid Sans Mono Slashed for Powerline")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_2.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.widget = QtWidgets.QWidget(Terminal)
        self.widget.setGeometry(QtCore.QRect(40, 20, 741, 31))
        self.widget.setObjectName("widget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setSizeIncrement(QtCore.QSize(5, 5))
        font = QtGui.QFont()
        font.setFamily("Droid Sans Mono for Powerline")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setMouseTracking(True)
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)


        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setSizeIncrement(QtCore.QSize(5, 5))
        font = QtGui.QFont()
        font.setFamily("Droid Sans Mono for Powerline")
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n""border:none\n""}")


        self.shortcut=QtWidgets.QShortcut(QtGui.QKeySequence("Return"),Terminal)
        self.currentDir=self.getDir()
        self.shortcut.activated.connect(self.commandExecute)

        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.retranslateUi(Terminal)
        QtCore.QMetaObject.connectSlotsByName(Terminal)

    def retranslateUi(self, Terminal):
        _translate = QtCore.QCoreApplication.translate
        Terminal.setWindowTitle(_translate("Terminal", "Terminal"))
        self.label_2.setText(_translate("Terminal", "WelCome In My Terminal"))
        self.label.setText(self.getDir())



    # for Getting current Directory
    def getDir(self):
        s="Atul# "+os.getcwd()+"$ "
        return s

    # for Executing Commands
    def commandExecute(self):
        command=self.lineEdit.text()
        if command=="clear":
            self.label_2.setText("")
        elif command[0:2]=="cd":
            try:
                if len(command)==2:
                    os.chdir('/home/atul/fool/')
                else:
                    os.chdir(command[3:])
                self.label_2.setText("Command is Successful")
                self.label_2.setStyleSheet("color:green")
            except:
                self.label_2.setStyleSheet("color:red")
                self.label_2.setText("Directory change Failed!\n\n")                
        else:
            os.system(command+" > /home/atul/fool/output 2>&1")
            suc="Command is Successful\n\n\n"
            output=""
            with open('/home/atul/fool/output','r') as file:
                output=file.read()
                file.close()
            if (output.find("not found")!=-1 and len(output)<=100) or (output.find("cannot access")!=-1 and len(output)<=100):
                self.label_2.setStyleSheet("color:red")
                self.label_2.setText("Command Failed!\n\n"+output)
            else:
                self.label_2.setStyleSheet("color:green")
                self.label_2.setText(suc+output)
        self.currentDir=self.getDir()
        self.label.setText(self.currentDir)
        self.lineEdit.setText("")

# Running Application
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Terminal = QtWidgets.QWidget()
    ui = Ui_Terminal()
    ui.setupUi(Terminal)
    Terminal.show()
    sys.exit(app.exec_())
