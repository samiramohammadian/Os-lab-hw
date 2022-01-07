from PySide6.QtUiTools import QUiLoader
from sympy import cot
from math import * 
from PySide6.QtWidgets import * 
from PySide6.QtGui import *
from PySide6.QtCore import *





class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load("cl.ui")
        self.ui.show()

        self.key = ""
        self.resalt = 0
        self.ui.btn_0.clicked.connect(self.number0)
        self.ui.btn_1.clicked.connect(self.number1)
        self.ui.btn_2.clicked.connect(self.number2) 
        self.ui.btn_3.clicked.connect(self.number3)
        self.ui.btn_4.clicked.connect(self.number4)
        self.ui.btn_5.clicked.connect(self.number5)
        self.ui.btn_6.clicked.connect(self.number6)
        self.ui.btn_7.clicked.connect(self.number7)
        self.ui.btn_8.clicked.connect(self.number8)
        self.ui.btn_9.clicked.connect(self.number9)

        self.ui.btn_AC.clicked.connect(self.AC)
        self.ui.btn_dot.clicked.connect(self.dot)
        self.ui.btn_inv.clicked.connect(self.inv)
        self.ui.btn_sum.clicked.connect(self.add)
        self.ui.btn_sub.clicked.connect(self.sub)
        self.ui.btn_cross.clicked.connect(self.cross)
        self.ui.btn_div.clicked.connect(self.div)
        self.ui.btn_per.clicked.connect(self.per)
        self.ui.btn_sin.clicked.connect(self.sin_func)
        self.ui.btn_cos.clicked.connect(self.cos_func)
        self.ui.btn_tan.clicked.connect(self.tan_func)
        self.ui.btn_cot.clicked.connect(self.cot_func)
        self.ui.btn_log.clicked.connect(self.log_func)
        self.ui.btn_sqrt.clicked.connect(self.sqrt_func)
        self.ui.btn_equal.clicked.connect(self.equal)

    def number0(self):
        self.ui.tb_1.setText(self.ui.tb_1.text() + "0")
    def number1(self):
        self.ui.tb_1.setText(self.ui.tb_1.text() + "1")
    def number2(self):
        self.ui.tb_1.setText(self.ui.tb_1.text() + "2")
    def number3(self):
        self.ui.tb_1.setText(self.ui.tb_1.text() + "3")
    def number4(self):
        self.ui.tb_1.setText(self.ui.tb_1.text() + "4")
    def number5(self):
        self.ui.tb_1.setText(self.ui.tb_1.text() + "5")
    def number6(self):
        self.ui.tb_1.setText(self.ui.tb_1.text() + "6")
    def number7(self):
        self.ui.tb_1.setText(self.ui.tb_1.text() + "7")
    def number8(self):
        self.ui.tb_1.setText(self.ui.tb_1.text() + "8")
    def number9(self):
        self.ui.tb_1.setText(self.ui.tb_1.text() + "9")

    def dot(self):
        if '.' not in self.ui.tb_1.text():
            self.ui.tb_1.setText(self.ui.tb_1.text() + '.')

    def AC(self):
       self.ui.tb_1.setText("")
       self.resalt=0
       self.key=""

    def inv(self):
        self.num2 = float(self.ui.tb_1.text())
        self.num2 *=-1
        self.ui.tb_1.setText(str(self.num2))

    def add(self):
        try:
            self.num1 = float(self.ui.tb_1.text())
            self.ui.tb_1.setText("")
            self.key ="+"
        except:
            self.ui.tb_1.setText(" ERROR !!! ") 
            self.key =""

    def sub(self):
        try:
            self.num1 = float(self.ui.tb_1.text())
            self.ui.tb_1.setText("")
            self.key ="-"
        except:
            self.ui.tb_1.setText(" ERROR !!! ") 
            self.key =""

    def cross(self):
        try:
            self.num1 = float(self.ui.tb_1.text())
            self.ui.tb_1.setText("")
            self.key ="*"
        except:
            self.ui.tb_1.setText(" ERROR !!! ") 
            self.key =""

    def div(self):
        try:
            self.num1 = float(self.ui.tb_1.text())
            self.ui.tb_1.setText("")
            self.key ="/"
        except:
            self.ui.tb_1.setText(" ERROR !!! ") 
            self.key =""

    def per(self):
        try:
            self.resalt = float(self.ui.tb_1.text())/100
            self.ui.tb_1.setText(str(self.resalt))
        except:
            self.ui.tb_1.setText(" ERROR !!! ") 
            self.key =""

    def sin_func(self):
        self.resalt = round(sin(radians(float(self.ui.tb_1.text()))), 4)
        self.ui.tb_1.setText(str(self.resalt))
  
    def cos_func(self):
        self.resalt = round(cos(radians(float(self.ui.tb_1.text()))), 4)
        self.ui.tb_1.setText(str(self.resalt)) 

    def tan_func(self):
        self.resalt = round(tan(radians(float(self.ui.tb_1.text()))), 4)
        self.ui.tb_1.setText(str(self.resalt)) 

    def cot_func(self):
        self.resalt = round(cot(radians(float(self.ui.tb_1.text()))), 4)
        self.ui.tb_1.setText(str(self.resalt)) 

    def log_func(self):
        self.resalt = round(log(float(self.ui.tb_1.text()), 10), 4)
        self.ui.tb_1.setText(str(self.resalt)) 

    def sqrt_func(self):
        self.resalt = round(sqrt(float(self.ui.tb_1.text())), 4)
        self.ui.tb_1.setText(str(self.resalt))

    def equal(self):
        try:
            self.num2 = float(self.ui.tb_1.text())
            self.ui.tb_1.setText("")
        except:
            self.ui.tb_1.setText(" ERROR !!! ") 
            self.key ="" 


        if self.key == "+": 
            self.resalt = self.num1 + self.num2
            self.ui.tb_1.setText(str(self.resalt))
        
        elif self.key == "-":
            self.resalt = self.num1 - self.num2
            self.ui.tb_1.setText(str(self.resalt))

        elif self.key == "*":
            self.resalt = self.num1 * self.num2
            self.ui.tb_1.setText(str(self.resalt)) 

        elif self.key == "/":
            self.resalt = self.num1 / self.num2
            self.ui.tb_1.setText(str(self.resalt)) 


if __name__ == "__main__":

    app = QApplication()
    main_window = Calculator()
    app.exec()



