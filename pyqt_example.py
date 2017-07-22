import sys
#import sip


#sip.setapi('QDate', 2)
#sip.setapi('QDateTime', 2)
#sip.setapi('QString', 2)
#sip.setapi('QTextStream', 2)
#sip.setapi('QTime', 2)
#sip.setapi('QUrl', 2)
#sip.setapi('QVariant', 2)

from PyQt4.QtCore import *
from PyQt4.QtGui import *

# Main Application Object
qt_app = QApplication(sys.argv)


class MyForm(QWidget):
	def __init__(self):
		super(MyForm, self).__init__()
		
		
		self.setWindowTitle("My Basic Form")
		self.buttonLabel = QLabel("Form Yet not submitted")
		self.lcd = QLCDNumber()
		self.slider = QSlider()
		self.slabel = QLabel("...")
		#lbl1.move(55,12)
		#lbl1.setAlignment(Qt.AlignCenter)
		#lbl2.move(55,18)
		#lbl2.setAlignment(Qt.AlignCenter)
		editor1 = QLineEdit("first name", self)
		#editor1.move(55,35)
		#lbl2 = QLabel("Last Name : ", self)
		#lbl3 = QLabel("Gender : ", self)
		#lbl4 = QLabel("Age : ", self)
		editor2 = QLineEdit("last name", self)
		#editor2.move(55,75)
		#editor1.setFixedWidth(200)
		#editor2.setFixedWidth(200)
		button1 = QPushButton("submit",self)
		#button1.move(95,215)
		gender = QComboBox()
		gender.addItems(['Male','Female'])
		
		age = QSpinBox()
		age.setMinimum(18)

#		layout = QGridLayout()
#		layout.addWidget(lbl1,0,0)
#		layout.addWidget(editor1,0,1)
#		layout.addWidget(lbl2,1,0)
#		layout.addWidget(editor2,1,1)
#		layout.addWidget(gender,2,1)
#		layout.addWidget(age,3,1)
#		layout.addWidget(button1,4,1)
#		layout.addWidget(lbl3,2,0)
#		layout.addWidget(lbl4,3,0)
				
		layout = QFormLayout()
		layout.addRow("First Name : ", editor1)
		layout.addRow("Last Name : ", editor2)
		layout.addRow("Gender : ",gender)
		layout.addRow("Age : ",age)
		layout.addRow(self.lcd)
		layout.addRow(self.slider)
		layout.addRow(self.slabel)
		layout.addRow(button1)
		#layout.addRow(buttonLabel)
		#self.lbl = QLabel('Form not submitted yet')
		layout.addRow(self.buttonLabel)
		


		self.setLayout(layout)
		self.setGeometry(700,300,300,400)
		#self._closeButton = QToolButton()
		#self._closeButton.setText("submit")
		#calender = QCalendarWidget(self)
		#calender.move(200,200)
		
		self.slider.sliderMoved.connect(self.handleSliderMove)
		self.slider.valueChanged.connect(self.lcd.display)
		button1.clicked.connect(self.handleClicked)
		
		self.show()


	def handleClicked(self):
		#self.buttonLabel.setText("Form Successfully Submitted")
		self.buttonLabel.setText('Form Successfully Submitted ')

	def handleSliderMove(self):
		self.slabel.setText("Slider in Motion ")


From1 = MyForm()


qt_app.exec_()























'''
class QtApp(QLabel):
        def __init__(self):
                QLabel.__init__(self, "Hello World !")
                
                #Setting size alignment etc
                self.setMinimumSize(QSize(600, 400))
                self.setAlignment(Qt.AlignCenter)
                self.setWindowTitle("Hello World")
                

        def run(self):
                self.show()
                qt_app.exec_()

'''


