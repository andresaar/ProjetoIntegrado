import serial as s
import time as t
com = ''

class Ferramenta:
    def __init__(self):
        self.F = 0
        self.G = 0
        self.T = 0
        self.D = 0
        self.R = 0
        self.P = 0
    def valores(self):
        print("F = " + str(self.F))
        print("G = " + str(self.G))
        print("T = " + str(self.T))
        print("D = " + str(self.D))
        print("R = " + str(self.R))
        print("P = " + str(self.P))


def ini(port):
    global com
    com = s.Serial(port,115200,timeout=0)
    return

string = ""
esq = Ferramenta()
dir = Ferramenta()

def atualiza():
    global com
    com.flushInput()
    com.write(1)
    t.sleep(.02)

    if com.inWaiting() > 0:
        try:
            string = com.readline().decode('utf-8')
            string = string.split('*')
            sum = 0
            for ch in string[0]:
                sum=sum+ord(ch)
            if sum != int(string[1]):
                return
            string = string[0].split('_')
            esq.F = int(string[0].strip("F"))
            esq.G = int(string[1].strip("G"))
            esq.T = int(string[2].strip("T"))
            esq.D = int(string[3].strip("D"))
            esq.R = int(string[4].strip("R"))
            esq.P = int(string[5].strip("P"))
            dir.F = int(string[6].strip("f"))
            dir.G = int(string[7].strip("g"))
            dir.T = int(string[8].strip("t"))
            dir.D = int(string[9].strip("d"))
            dir.R = int(string[10].strip("r"))
            dir.P = int(string[11].strip("p"))

        except:
           return
    else:
        return

def valores_esq():
    atualiza()
    return [esq.F, esq.G, esq.T, esq.D, esq.R, esq.P]

def valores_dir():
    atualiza()
    return [dir.F, dir.G, dir.T, dir.D, dir.R, dir.P]

def encerra():
    com.close()
    return

def abre():
    com.open()
    return