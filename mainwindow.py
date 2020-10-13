from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particulas import Particulas
from particula import Particula

particulas = Particulas()
particula  = Particula()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        ui = Ui_MainWindow()
        ui.setupUi(self)
 
        ui.Capturar.clicked.connect(self.click_agregar)
        ui.Mostrar.clicked.connect(self.click_mostrar)
        ui.ID.valueChanged.connect(self.setValue)
        ui.Velocidad.valueChanged.connect(self.setValue)
        ui.OrigenX.valueChanged.connect(self.slider_value)
        ui.OrigenY.valueChanged.connect(self.slider_value)
        ui.DestinoX.valueChanged.connect(self.slider_value)
        ui.DestinoY.valueChanged.connect(self.slider_value)
        ui.Rojo.valueChanged.connect(self.slider_value)
        ui.Verde.valueChanged.connect(self.slider_value)
        ui.Azul.valueChanged.connect(self.slider_value) 
    
    @Slot()
    def setValue(self,valor):
        print(valor) 

    @Slot()
    def slider_value(self,valor1):
        print(valor1)  
                            
    @Slot()
    def click_mostrar(self):
        print('mostrar')
        particulas.mostrar() 

    @Slot()
    def click_agregar(self):
        print('Particula Capturada')               
        particulas.agregar_inicio(particula)

p1  = Particula("2","2","0","0","0","0","0","0","0")
particulas.agregar_final(p1)  