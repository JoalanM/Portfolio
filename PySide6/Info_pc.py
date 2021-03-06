from PySide6 import QtWidgets
import os
import platform
import sys
import socket
import uuid
import requests
from PySide6 import QtGui, QtCore

class MaFenetre(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
#        self.resize()
        self.setWindowTitle("Computer information")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        self.setup_connections()
        self.main_widget()
    
    def create_layouts(self):
        self.layoutV1 = QtWidgets.QVBoxLayout()
        self.layoutV2 = QtWidgets.QVBoxLayout()
        self.layoutV3 = QtWidgets.QVBoxLayout()
        self.layoutV4 = QtWidgets.QVBoxLayout()
        self.layoutH7 = QtWidgets.QHBoxLayout()
        self.layoutH8 = QtWidgets.QHBoxLayout()
        self.layoutH9 = QtWidgets.QHBoxLayout()
        self.layoutV5 = QtWidgets.QVBoxLayout()
        

    def create_widgets(self):
        self.label_computer = QtWidgets.QLabel("Computer informations")
        self.label_computer.setStyleSheet('color:#0000FF')
        self.label_computer.setFont(QtGui.QFont("Sanserif",20))
        self.setWindowIcon(QtGui.QIcon(r'E:\pythonCode\1024.png'))


        self.label_hostname = QtWidgets.QLabel("Hostname")
        self.edit_hostname = QtWidgets.QLineEdit()

        self.label_lan = QtWidgets.QLabel("LAN IP Adress")
        self.edit_lan = QtWidgets.QLineEdit()

        self.label_mac = QtWidgets.QLabel("MAC Adress")
        self.edit_mac = QtWidgets.QLineEdit()

        self.label_wan = QtWidgets.QLabel("WAN IP Adress")
        self.edit_wan = QtWidgets.QLineEdit()

        self.label_system = QtWidgets.QLabel("System")
        self.edit_system = QtWidgets.QLineEdit()

        self.btn_quitter = QtWidgets.QPushButton("Exit")

    def addWigets_to_layouts(self):
        self.layoutV1.addWidget(self.label_computer)

        self.layoutV2.addWidget(self.label_hostname)
        self.layoutV3.addWidget(self.edit_hostname)

        self.layoutV2.addWidget(self.label_lan)
        self.layoutV3.addWidget(self.edit_lan)

        self.layoutV2.addWidget(self.label_mac)
        self.layoutV3.addWidget(self.edit_mac)

        self.layoutV2.addWidget(self.label_wan)
        self.layoutV3.addWidget(self.edit_wan)

        self.layoutV2.addWidget(self.label_system)
        self.layoutV3.addWidget(self.edit_system)
        
        self.layoutV4.addWidget(self.btn_quitter)

        self.layoutH7.addLayout(self.layoutV1)
        self.layoutH8.addLayout(self.layoutV2)
        self.layoutH8.addLayout(self.layoutV3)
        self.layoutH9.addLayout(self.layoutV4)

        self.layoutV5.addLayout(self.layoutH7)
        self.layoutV5.addLayout(self.layoutH8)
        self.layoutV5.addLayout(self.layoutH9)


    def main_widget(self):
        self.widget = QtWidgets.QWidget(self)  
        
        self.widget.setLayout(self.layoutV5)
        self.setCentralWidget(self.widget)

    def setup_connections(self):
        self.btn_quitter.clicked.connect(quit)

        #------------------------------------------------------------------#
        #NOM
        self.edit_hostname.setText(str(socket.gethostname()))
        #SYSTEME
        self.edit_system.setText(str(platform.system()))
        #MAC ADRESS
        self.edit_mac.setText(str(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)for ele in range (0,8*6,8)][::-1])))
        #LAN IP ADRESS
        hostname = socket.gethostname()
        ip_add=socket.gethostbyname(hostname)
        self.edit_lan.setText(str(ip_add))

        print(requests.get('http://ip.42.pl/raw').text)
        self.edit_wan.setText(str(requests.get('http://ip.42.pl/raw').text))

        # print(os.name)
        # print(platform.uname)
        



if __name__ == '__main__':
    # Create the Qt Application
    app = QtWidgets.QApplication([])
    # Create and show the form
    form = MaFenetre()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
    # app.exec()