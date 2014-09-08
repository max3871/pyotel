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
		name_class = self.field("name")
		mail_class = self.field("mail")
		age_class = self.field("age")
		
		print(age_class)
		print(mail_class)
		print(name_class)
		
		super(monAssistant, self).accept()

    

class IntroPage(QWizardPage):
	def __init__(self, parent=None):
		super(IntroPage, self).__init__(parent)
		self.setTitle("Bienvenue")
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




		rx = QRegExp("""[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?""")
		validator = QRegExpValidator(rx, self)
		mailLabel = QLabel("&Email : ")
		mailEdit = QLineEdit()
		mailEdit.setValidator(validator)
		mailLabel.setBuddy(mailEdit)

		ageLabel = QLabel("Age : ")
		ageEdit = QSpinBox()
		ageEdit.setRange(18, 100)
		ageEdit.setSuffix(" ans")

		self.registerField("name*", nameEdit)
		self.registerField("mail", mailEdit)
		self.registerField("age", ageEdit)

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


		self.nameLabel = QLabel()
		self.mailLabel = QLabel()
		self.ageLabel = QLabel()

		layout = QVBoxLayout()
		layout.addWidget(label)
		layout.addWidget(self.nameLabel)
		layout.addWidget(self.mailLabel)
		layout.addWidget(self.ageLabel)
		self.setLayout(layout)
	def initializePage(self):
		name_class = self.field("name")
		mail_class = self.field("mail")
		age_class = self.trUtf8(str(self.field("age")))

		self.nameLabel.setText(name_class)
		self.mailLabel.setText(mail_class)
		self.ageLabel.setText(age_class)

if __name__=="__main__":
	a=QApplication(sys.argv)
	translatorFileName = "qt_"
	translatorFileName += QLocale.system().name()
	translator = QTranslator(a)
	if translator.load(translatorFileName, QLibraryInfo.location(QLibraryInfo.TranslationsPath)):
		a.installTranslator(translator)

	f = monAssistant()
	f.setWindowTitle("Mon premier assistant")
	f.show()
	a.exec_()
