#Esse programa testa as entradas do Raspberry-Pi 3 em modo BCM
#O botao devera ser conectado ao terra. Os resistores internos de pull-up estao ativados
#Quando o botao for pressionado, sera exibida uma mensagem na tela mostrando sua posicao

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:

 state2 = GPIO.input(2)
 state3 = GPIO.input(3)
 state4 = GPIO.input(4)
 state5 = GPIO.input(5)
 state6 = GPIO.input(6)
 state7 = GPIO.input(7)
 state8 = GPIO.input(8)
 state9 = GPIO.input(9)
 state10 = GPIO.input(10)
 state11 = GPIO.input(11)
 state12 = GPIO.input(12)
 state13 = GPIO.input(13)
 state14 = GPIO.input(14)
 state15 = GPIO.input(15)
 state16 = GPIO.input(16)
 state17 = GPIO.input(17)
 state18 = GPIO.input(18)
 state19 = GPIO.input(19)
 state20 = GPIO.input(20)
 state21 = GPIO.input(21)
 state22 = GPIO.input(22)
 state23 = GPIO.input(23)
 state24 = GPIO.input(24)
 state25 = GPIO.input(25)
 state26 = GPIO.input(26)
 state27 = GPIO.input(27)

 if state2 == False:
    print('Button 2')
    time.sleep(0.2)

 if state3 == False:
    print('Button 3')
    time.sleep(0.2)

 if state4 == False:
    print('Button 4')
    time.sleep(0.2)

 if state5 == False:
    print('Button 5')
    time.sleep(0.2)

 if state6 == False:
    print('Button 6')
    time.sleep(0.2)

 if state7 == False:
    print('Button 7')
    time.sleep(0.2)

 if state8 == False:
    print('Button 8')
    time.sleep(0.2)

 if state9 == False:
    print('Button 9')
    time.sleep(0.2)

 if state10 == False:
    print('Button 10')
    time.sleep(0.2)

 if state11 == False:
    print('Button 11')
    time.sleep(0.2)

 if state12 == False:
    print('Button 12')
    time.sleep(0.2)

 if state13 == False:
    print('Button 13')
    time.sleep(0.2)

 if state14 == False:
    print('Button 14')
    time.sleep(0.2)

 if state15 == False:
    print('Button 15')
    time.sleep(0.2)

 if state16 == False:
    print('Button 16')
    time.sleep(0.2)

 if state17 == False:
    print('Button 17')
    time.sleep(0.2)

 if state18 == False:
    print('Button 18')
    time.sleep(0.2)

 if state19 == False:
    print('Button 19')
    time.sleep(0.2)

 if state20 == False:
    print('Button 20')
    time.sleep(0.2)

 if state21 == False:
    print('Button 21')
    time.sleep(0.2)

 if state22 == False:
    print('Button 22')
    time.sleep(0.2)

 if state23 == False:
    print('Button 23')
    time.sleep(0.2)

 if state24 == False:
    print('Button 24')
    time.sleep(0.2)

 if state25 == False:
    print('Button 25')
    time.sleep(0.2)

 if state26 == False:
    print('Button 26')
    time.sleep(0.2)

 if state27 == False:
    print('Button 27')
    time.sleep(0.2)
