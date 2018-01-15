import sys
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.task import Task
import OptionGUI as op
import Com as c

i=1
aumenta = True
loadPrcFile('conf.prc')

class Window(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.loadModel()
        self.setBackgroundColor(0, 0, 0)
        self.lights()
        if op.cf:
            self.disableMouse()
            if op.esq:
                self.camera.reparentTo(self.haste1)
                self.camera.setHpr(-90, 0, 0)
                self.camera.setPos(-15, 0, 0)
                self.tesoura11.hide()
                self.tesoura12.hide()
            else:
                self.camera.reparentTo(self.haste2)
                self.camera.setHpr(-90, 0, 180)
                self.camera.setPos(-15, 0, 0)
                self.tesoura21.hide()
                self.tesoura22.hide()
        else:
            self.useTrackball()
        taskMgr.doMethodLater(.02, muda, 'teste')
        self.acceptOnce("escape", self.userExit)

    def loadModel(self):
        self.haste1 = loader.loadModel("haste.egg")
        self.haste2 = loader.loadModel("haste.egg")
        self.join1 = loader.loadModel("bola.egg")
        self.join2 = loader.loadModel("bola.egg")
        self.join1.reparentTo(render)
        self.join2.reparentTo(render)
        self.haste1.reparentTo(self.join1)
        self.haste2.reparentTo(self.join2)
        self.join1.setPos(-15, 50, 15)
        self.join2.setPos(15, 50, 15)
        self.join1.setHpr(45,0,45) # Z, X, Y
        self.join2.setHpr(-45, 0, 135)
        self.tesoura11 = loader.loadModel("tesoura.egg")
        self.tesoura11.reparentTo(self.haste1)
        self.tesoura11.setPos(0.2, .05, 0)
        self.tesoura11.setHpr(120,180,180) #primeiro entre 90 e 180
        self.tesoura12 = loader.loadModel("tesoura.egg")
        self.tesoura12.reparentTo(self.haste1)
        self.tesoura12.setPos(0.2, -0.05, 0)
        self.tesoura12.setHpr(60, 180, 0) #primeiro angulo menor q 90
        self.tesoura21 = loader.loadModel("tesoura.egg")
        self.tesoura21.reparentTo(self.haste2)
        self.tesoura21.setPos(0.2, .05, 0)
        self.tesoura21.setHpr(120, 180, 180)  # primeiro entre 90 e 180
        self.tesoura22 = loader.loadModel("tesoura.egg")
        self.tesoura22.reparentTo(self.haste2)
        self.tesoura22.setPos(0.2, -0.05, 0)
        self.tesoura22.setHpr(60, 180, 0)  # primeiro angulo menor q 90
        self.fundo = loader.loadModel("fundo.egg")
        self.fundo.reparentTo(render)
        self.fundo.setPos(0,65,-8)

    def lights(self):
        ambient = AmbientLight('ambient')
        ambient.setColor(VBase4(0.05,0.05,0.05,1))
        ambientNP = render.attachNewNode(ambient)
        render.setLight(ambientNP)
        pl = PointLight('pl')
        pl.setColor(VBase4(.8,.8,.8,.5))
        pl.setAttenuation((0.5, 0, 0))
        self.plnp = self.camera.attachNewNode(pl)
        render.setLight(self.plnp)

    def tesoura(self,angulo):
        self.tesoura11.setH(90+angulo/2)
        self.tesoura12.setH(90-angulo/2)

    def tesoura2(self,angulo):
        self.tesoura21.setH(90+angulo/2)
        self.tesoura22.setH(90-angulo/2)



def muda(task):
    global i, aumenta
    game.tesoura2(30 * i / 100)
    game.haste2.setPos(i * 25 / 100, 0, 0)
    haste1 = c.valores_esq()
    game.join1.setHpr((haste1[1]-416)*130/(1023-416), 0, -5+(haste1[0]-74)*110/(220-74))
    game.haste1.setP(-((haste1[2]-16)*270/(1024-16)+haste1[4]*20))
    game.haste1.setPos(20*haste1[3]/392,0,0)
    game.tesoura((haste1[5]-71)*30/(113-71))
    if aumenta==True:
        i=i+1
    else:
        i=i-1
    if i == 101:
        aumenta = False
    if i == 1:
        aumenta = True
    return task.again

if op.com == "":
    exit(1)
c.ini(op.com)
game = Window()
game.run()
