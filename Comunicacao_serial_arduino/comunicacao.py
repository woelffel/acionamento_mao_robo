import pyserial as serial

#### Comecar comunicacao serial
porta_usb = "USB0"
conexao = serial.Serial('/dev/' + porta_usb, 9600)

#### Averiguando se conexao relamente esta aberta
if (conexao.isOpen()):
    status_conexao = True
