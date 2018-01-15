import sys
import serial
import PyQt5.QtWidgets  as qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *

cf = False
esq = False
com = "perro"

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    else:
        raise EnvironmentError('Unsupported platform')
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def sai():
    global cf, esq, com
    if com_sel.currentText() == "":
        com = "Nao há"
        print(com + "  " + str(cf) + "   " + str(esq))
        w.close()
        return app.exit(0)
    com = com_sel.currentText()
    if r1.isChecked():
        cf = True
        if fer_sel.currentText() == "Esquerda":
            esq = True
    print(com + "  " + str(cf) + "   " + str(esq)+"  "+str(w.size()))
    w.close()
    return app.exit(0)


app = qt.QApplication(sys.argv)
w = qt.QWidget()
w.setWindowTitle("Simulação Config")
w.move(300,300)
config = qt.QGroupBox(w)
layout = qt.QGridLayout()
com_sel = qt.QComboBox()
for port in serial_ports():
    com_sel.addItem(port)
com_l=qt.QLabel()
com_l.setText("COM")
com_l.setAlignment(Qt.AlignCenter)
layout.addWidget(com_l,0,0)
layout.addWidget(com_sel,0,1)
r1 = qt.QRadioButton("Câmera-Ferramenta")
r1.setChecked(True)
layout.addWidget(r1,1,0)
r2 = qt.QRadioButton("Câmera-Virtual")
layout.addWidget(r2,1,1)
config.setTitle("Configurações")
config.setLayout(layout)

fer_l=qt.QLabel()
fer_l.setText("Camera-Ferramenta")
fer_l.setAlignment(Qt.AlignCenter)
layout.addWidget(fer_l,2,0)
fer_sel = qt.QComboBox()
fer_sel.addItem('Esquerda')
fer_sel.addItem('Direita')
layout.addWidget(fer_sel,2,1)

btn = qt.QPushButton("Começar")
btn.clicked.connect(sai)
layout.addWidget(btn, 3,0,1,2)


w.resize(244,135)
w.show()
app.exec_()

