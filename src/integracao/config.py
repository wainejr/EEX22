import portDefines as pd
import RPi.GPIO as gpio

def configGPIOs():
    gpio.setmode(gpio.BOARD)
    
    # out GPIO
    for port in pd.GPIO_PORTS_OUT:
        gpio.setup(port, gpio.OUT)
        gpio.output(port, gpio.LOW) # mantem as portas de saida em nivel baixo por padrao inicialmente    
    
    # encoder
    gpio.setup(pd.GPIO_PORT_IN_ENC_SIG1, gpio.IN, pull_up_down=gpio.PUD_UP)
    gpio.setup(pd.GPIO_PORT_IN_ENC_SIG2, gpio.IN, pull_up_down=gpio.PUD_UP)

    # fim de curso
    gpio.setup(pd.GPIO_PORT_IN_FDC_LOWER, gpio.IN, pull_up_down=gpio.PUD_UP)
    gpio.setup(pd.GPIO_PORT_IN_FDC_UPPER, gpio.IN, pull_up_down=gpio.PUD_UP)

    # ultrassonico
    gpio.setup(pd.GPIO_PORT_IN_ULTR_ECHO, gpio.IN)

    print('Raspberry configurada')

def resetGPIOs():
    for port in pd.GPIO_PORTS_OUT:
        gpio.output(port, gpio.LOW)
    gpio.cleanup()

    print('Raspberry cleanup')

configGPIOs()