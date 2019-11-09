import config as cf
from movimentation import Movimentation
from parafusadeira import Parafusadeira
from servo import Servo
from camera import Camera
import time
import globals


class AGV:
    def __init__(self):
        print("Criando o AGV...")
        self.movimentation = Movimentation()
        self.servo = Servo()
        self.camera = Camera()
        self.parafusadeira = Parafusadeira()
        self.parafusadeira.config()
        self.log = {'Parafusos': [], 'Distancia percorrida': 0, 'Fotos analisadas': 0, 'Objetos na frente': 0}

    def tem_parafuso_para_apertar(self, angulo):
        self.move(30, globals.MEIO)
        self.apertar(angulo)

    def andar_e_verificar(self):
        while self.movimentation.encoder.position < 40:
            self.movimentation.stop()
            angulo = 0#self.verificar_parafuso()
            self.log['Fotos analisadas'] += 1
            self.move(5, globals.CIMA)
            if angulo is not None:
                self.log['Parafusos'].append({'Posicao': self.movimentation.encoder.data(), 'Angulo': angulo })
                if angulo >= 15 and angulo <= 165:
                    self.tem_parafuso_para_apertar(angulo)

    def move(self, distance, parafusadeira_position):
        if self.parafusadeira.position != parafusadeira_position:
            if parafusadeira_position == globals.CIMA:
                self.parafusadeira.subir()
            else:
                self.parafusadeira.metade()
        self.movimentation.move(distance)

    def apertar(self, graus):
        self.movimentation.stop()
        print("Preparando para apertar", graus, "graus...")
        self.servo.setAngle(graus)
        self.parafusadeira.descer()
        self.servo.apertar()
        self.parafusadeira.subir()

    def inicio(self):
        self.parafusadeira.subir()
        self.movimentation.inicio()

    def verificar_parafuso(self):
        return self.camera.verificar()

    def kill(self):
        self.log['Distancia percorrida'] = self.movimentation.encoder.data()
        self.log['Objetos na frente'] = self.movimentation.objetos_encontrados()
        print("\nEncerrando as atividades do AGV ...")
        self.movimentation.kill_threads()
        time.sleep(2)
        cf.resetGPIOs()
        print("Atividade do AGV encerradas!\n")
        return self.log
