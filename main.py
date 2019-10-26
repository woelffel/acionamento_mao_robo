from funcoes.comunic_pc_ard import arduino
from funcoes.captura_img_cam import opencv
import cv2
import keras

#### Abrindo conexao 
con = arduino.abrir_conexao("COM3")

#### Load no modelo
model = keras.models.load_model("C:/Engenharia/Git/acionamento_mao_robo/model.h5")
#### Checando conexao
if (con[1]):
    #### Abrindo camera
    cam = opencv.init_camera()
    #### Captura de frame
    frame = opencv.captura_frame(cam)
    #### Mostra imagem
    cv2.imshow('image', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#### Finaliza a conexao com a camera
opencv.finalizar_camera(cam)