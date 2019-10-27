import RPi.GPIO as gpio
import portDefines as pd
import time
import threading

class Encoder(threading.Thread):
    def __init__(self):
        print('Criando encoder')
        threading.Thread.__init__(self)
        self.position = 0
        self.state = [(1, 1), (0, 1), (0, 0), (1, 0)]
        self.last_a = 1
        self.last_b = 1
        self.curr_state = [i for i in range(0, len(self.state)) if self.state[i] == (self.last_a, self.last_b)][0]
        self.last_state = self.curr_state
        self.kill_flag = None
        self.start()

    def run(self):
        self.kill_flag = False
        while(not self.kill_flag):
            self.enc_a = gpio.input(pd.GPIO_PORT_IN_ENC_SIG1)
            self.enc_b = gpio.input(pd.GPIO_PORT_IN_ENC_SIG2)
            time.sleep(0.001)
            if(self.enc_a == 1):
                if(self.enc_b == 1):
                    self.curr_state = 0
                else:
                    self.curr_state = 3
            else:
                if(self.enc_b == 1):
                    self.curr_state = 1
                else:
                    self.curr_state = 2
        
            if(self.last_state != self.curr_state):
                if(self.curr_state == 0):
                    if(self.last_state == 3):
                        self.position -= 1
                    elif(self.last_state == 1):
                        self.position += 1
                self.last_state = self.curr_state

    def data(self):
        return self.position

    def kill(self):
        self.kill_flag = True


