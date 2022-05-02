import sys
from PySide6 import QtGui
from PySide6 import QtWidgets
from PySide6.QtCore import QDate, QTime
from PySide6.QtGui import QPixmap

from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication, QVBoxLayout, QDialog, QLabel, QHBoxLayout, QMessageBox)

import sqlite3

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form,self).__init__(parent)


        #Création de widgets


        #Création label (titre zone saisie)
        self.label_nom = QLabel("Nom :")
        self.label_prenom = QLabel("Prénom :")
        self.label_taille = QLabel("Taille :")
        self.label_poids = QLabel("Poids :")
        self.label_imc = QLabel("")
        
        #Création QLineEdit (zone saisie)
        self.edit_nom = QLineEdit("") #Création de la zone de saisie
        self.edit_nom.setPlaceholderText("MYRTIL") # Texte en transparant pour aider l'utilisateur 
        self.edit_prenom = QLineEdit("") #Création de la zone de saisie
        self.edit_prenom.setPlaceholderText("Joalan") # Texte en transparant pour aider l'utilisateur
        self.edit_taille = QLineEdit("") #Création de la zone de saisie
        self.edit_taille.setPlaceholderText("178") # Texte en transparant pour aider l'utilisateur 
        self.edit_poids = QLineEdit("") #Création de la zone de saisie
        self.edit_poids.setPlaceholderText("78") # Texte en transparant pour aider l'utilisateur

        #importation image
        self.label=QtWidgets.QLabel()
        pixmap = QtGui.QPixmap("C:/Users/utilisateur/Desktop/progr/PySide6/imc.jpg")
        self.label.setPixmap(pixmap)

        #Recupération heure
        self.date = QDate.currentDate()
        self.d = QDate(22,10,2021)
        
        #Création de button 
        self.button_calculer = QPushButton("Calculer")
        self.button_effacer = QPushButton("Effacer")

        #Organisation des widgets avec des layout
        layoutVer = QVBoxLayout()
        layoutHor1 = QHBoxLayout()
        layoutHor2 = QHBoxLayout()
        layoutHor3 = QHBoxLayout()
        layoutHor4 = QHBoxLayout()
        layoutHor5 = QHBoxLayout()
        layoutHor6 = QHBoxLayout()
        layoutHor7 = QHBoxLayout()
      

        
        

        layoutHor1.addWidget(self.label_nom)
        layoutHor1.addWidget(self.edit_nom)

        layoutHor2.addWidget(self.label_prenom)
        layoutHor2.addWidget(self.edit_prenom)

        layoutHor3.addWidget(self.label_taille)
        layoutHor3.addWidget(self.edit_taille)

        layoutHor4.addWidget(self.label_poids)
        layoutHor4.addWidget(self.edit_poids)

        layoutHor5.addWidget(self.button_calculer)
        layoutHor5.addWidget(self.button_effacer)

        layoutHor6.addWidget(self.label)
        layoutHor7.addWidget(self.label_imc)

      
        layoutVer.addLayout(layoutHor6)
        layoutVer.addLayout(layoutHor1)
        layoutVer.addLayout(layoutHor2)
        layoutVer.addLayout(layoutHor3)
        layoutVer.addLayout(layoutHor4)
        layoutVer.addLayout(layoutHor5)
        layoutVer.addLayout(layoutHor7)
        
        

        # layoutVer.addWidget(self.label_resultat)
        self.setLayout(layoutVer)

        self.button_calculer.clicked.connect(self.calculer)
        self.button_effacer.clicked.connect(self.effacer)
        self.messagebox = QMessageBox()
        self.messagebox.setText("Erreur de calcul")
        

    def calculer(self): 
        self.button_calculer.clicked.connect(self.GET_DATA)

    def GET_DATA(self):
        db=sqlite3.connect

    def effacer(self):
        self.label_prenom.setText("")
        self.edit_nom.setText("")
        self.edit_taille.setText("")
        self.edit_poids.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = Form()
    form.show()
    sys.exit(app.exec())

        