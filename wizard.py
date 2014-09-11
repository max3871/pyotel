#!/usr/bin/python3
# -*- coding: utf-8 -*-


from PySide.QtCore import *
from PySide.QtGui import *

import sys


class monAssistant(QWizard):
	def __init__(self, parent=None):
		super(monAssistant, self).__init__(parent)

		self.addPage(IntroPage())
		self.addPage(RegistrationPage())
		self.addPage(ConclusionPage())
		self.setWizardStyle(QWizard.ModernStyle)

	def accept(self):
		
		
		super(monAssistant, self).accept()

    

class IntroPage(QWizardPage):
	def __init__(self, parent=None):
		super(IntroPage, self).__init__(parent)
		self.setTitle("Bienvenue sur Pyotel")
		self.setSubTitle("Bienvenue")

		label = QLabel(self.trUtf8("Première page de notre assitant"))
		
		label.setWordWrap(True)
		texte = QTextEdit()
		texte.setReadOnly(1)
		texte.setText(open('COPYRIGHT.txt').read())

		layout = QVBoxLayout()
		layout.addWidget(label)
		layout.addWidget(texte)
		self.setLayout(layout)

class RegistrationPage(QWizardPage):
	def __init__(self, parent=None):
		super(RegistrationPage, self).__init__(parent)

		self.setTitle("Enregistrement")

		label = QLabel("Deuxième page de notre assitant")
		label.setWordWrap(True)

		nameLabel = QLabel("Nom : ")
		nameEdit = QLineEdit()




		

		layout = QVBoxLayout()
		layout.addWidget(label)
		layout.addWidget(nameLabel)
		layout.addWidget(nameEdit)
		layout.addWidget(mailLabel)
		layout.addWidget(mailEdit)
		layout.addWidget(ageLabel)
		layout.addWidget(ageEdit)
		self.setLayout(layout)

class ConclusionPage(QWizardPage):
	def __init__(self, parent=None):
		super(ConclusionPage, self).__init__(parent)

		self.setTitle("Conclusion")

		label = QLabel("Dernière page de notre assitant")
		label.setWordWrap(True)


		

if __name__=="__main__":
	a=QApplication(sys.argv)
	translatorFileName = "qt_"
	translatorFileName += QLocale.system().name()
	translator = QTranslator(a)
	if translator.load(translatorFileName, QLibraryInfo.location(QLibraryInfo.TranslationsPath)):
		a.installTranslator(translator)

	f = monAssistant()
	f.setWindowTitle("Assistant de congiguration de Pyotel")
	f.show()
	a.exec_()
