import ports
# import RPi.GPIO as gpio
import time
import globals

class Parafusadeira():
    def __init__(self, config=True):
        print('Criando parafusadeira')
        self.position = None
        self.half_duration = None
        self.configured = False
        if config:
            self._config()

    def _config(self):
        print('configurando a parafusadeira')
        if not self.configured:
            self.descer()
            init_time = time.time()
            self.subir()
            self.half_duration = (time.time() - init_time)/2
            self.configured = True
        print('configurou a parafusadeira. tempo metade', self.half_duration, 'segundos')

    def metade(self):
        print('posicionando parafusadeira na metade')
        # if self.position == globals.CIMA:
        #     gpio.output(ports.GPIO_PORT_OUT_PARAF_EN, gpio.HIGH) #enable on
        #     gpio.output(ports.GPIO_PORT_OUT_PARAF_SIG1, gpio.LOW)
        #     gpio.output(ports.GPIO_PORT_OUT_PARAF_SIG2, gpio.HIGH)
            
        #     if self.configured:
        #         time.sleep(self.half_duration * .64)
        #     else:
        #         time.sleep(1 * .64)

        # elif self.position == globals.BAIXO:
        #     gpio.output(ports.GPIO_PORT_OUT_PARAF_EN, gpio.HIGH) #enable on
        #     gpio.output(ports.GPIO_PORT_OUT_PARAF_SIG1, gpio.HIGH)
        #     gpio.output(ports.GPIO_PORT_OUT_PARAF_SIG2, gpio.LOW)
        #     if self.configured:
        #         time.sleep(self.half_duration * 1.36)
        #     else:
        #         time.sleep(1 * 1.36)
        
        # gpio.output(ports.GPIO_PORT_OUT_PARAF_EN, gpio.LOW) #enable on
        # gpio.output(ports.GPIO_PORT_OUT_PARAF_SIG1, gpio.LOW)
        # gpio.output(ports.GPIO_PORT_OUT_PARAF_SIG2, gpio.LOW)
        self.position = globals.MEIO
        print('posicionou parafusadeira na metade')

    def subir(self):
        print('posicionando parafusadeira em cima')
        # while(gpio.input(ports.GPIO_PORT_IN_FDC_UPPER) == gpio.HIGH):
        #     gpio.output(ports.GPIO_PORT_OUT_PARAF_EN, gpio.HIGH) #enable on
        #     gpio.output(ports.GPIO_PORT_OUT_PARAF_SIG1, gpio.HIGH)
        #     gpio.output(ports.GPIO_PORT_OUT_PARAF_SIG2, gpio.LOW)
        # gpio.output(ports.GPIO_PORT_OUT_PARAF_EN, gpio.LOW) #enable on
        # gpio.output(ports.GPIO_PORT_OUT_PARAF_SIG1, gpio.LOW)
        # gpio.output(ports.GPIO_PORT_OUT_PARAF_SIG2, gpio.LOW)
        self.position = globals.CIMA
        print('posicionou parafusadeira em cima')

    def descer(self):
        print('posicionando parafusadeira em baixo')
        # while(gpio.input(ports.GPIO_PORT_IN_FDC_LOWER) == gpio.HIGH):
        #     gpio.output(ports.GPIO_PORT_OUT_PARAF_EN, gpio.HIGH) #enable on
        #     gpio.output(ports.GPIO_PORT_OUT_PARAF_SIG1, gpio.LOW)
        #     gpio.output(ports.GPIO_PORT_OUT_PARAF_SIG2, gpio.HIGH)
        # gpio.output(ports.GPIO_PORT_OUT_PARAF_EN, gpio.LOW) #enable on
        # gpio.output(ports.GPIO_PORT_OUT_PARAF_SIG1, gpio.LOW)
        # gpio.output(ports.GPIO_PORT_OUT_PARAF_SIG2, gpio.LOW)
        self.position = globals.BAIXO
        print('posicionou parafusadeira em baixo')
    
