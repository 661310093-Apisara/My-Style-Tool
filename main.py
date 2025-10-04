try:
	from PySide6 import QtCore, QtGui ,QtWidgets
	from shiboken6 import wrapInstance
except :
	from PySide2 import QtCore,QtGui,QtWidgets
	from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui

ROOT_RESOURCE_DIR = 'C:/Users/ICT68/Documents/maya/2025/scripts/myStyleTool'

class MyStyleToolDialog(QtWidgets.QDialog):
	def __init__(self,parent=None):
		super().__init__(parent)

		self.setWindowTitle('My Tool')
		self.resize(300,100)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet('background-color:#052A59;')

		self.imageLabel = QtWidgets.QLabel()
		self.imagePixmap = QtGui.QPixmap(f'{ROOT_RESOURCE_DIR}/image/cat.png')
		self.imageLabel.setPixmap(self.imagePixmap)
		self.mainLayout.addWidget(self.imageLabel)

		self.nameLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.nameLayout)
		self.nameLabel = QtWidgets.QLabel('Name : ')
		self.nameLineEdit = QtWidgets.QLineEdit()
		self.nameLayout.addWidget(self.nameLabel)
		self.nameLayout.addWidget(self.nameLineEdit)

		self.buttonLayout = QtWidgets.QHBoxLayout()

		self.mainLayout.addLayout(self.buttonLayout)
		self.CreateButton = QtWidgets.QPushButton('Create')
		self.CreateButton.setStyleSheet(
			'''
				QPushButton{
					background-color:#4968A6;
					color: white;
					border-radius: 10px;
					font-size:16px;
					padding: 8px;
					font-family: Papyrus ;
					font-weight: bold;
				}

				QPushButton:hover{
					background-color: qlineargradient(x1:0, y1:0,x2:1,y2:1,stop:0 #4968A6, stop:1 #3FBFBF);
				}

				QPushButton:pressed{
					background-color:#3FBFBF;
				}
			'''
			)

		self.CancelButton = QtWidgets.QPushButton('Cancel')
		self.CancelButton.setStyleSheet(
			'''
				QPushButton{
					background-color:#4968A6;
					color: white;
					border-radius: 10px;
					font-size:16px;
					padding: 8px;
					font-family: Papyrus ;
					font-weight: bold;
				}

				QPushButton:hover{
					background-color: qlineargradient(x1:0, y1:0,x2:1,y2:1,stop:0 #4968A6, stop:1 #3FBFBF);
				}

				QPushButton:pressed{
					background-color:#3FBFBF;
				}
			'''
			)

		self.buttonLayout.addWidget(self.CreateButton)
		self.buttonLayout.addWidget(self.CancelButton)

		self.mainLayout.addStretch()





def run():
	global ui
	try:
		ui.close()
	except:
		pass
	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()),QtWidgets.QWidget)
	ui = MyStyleToolDialog(parent=ptr)
	ui.show()