from funcoes.comunic_pc_ard import arduino
from funcoes.captura_img_cam import opencv
import cv2
from tensorflow import keras as K
import tensorflow as tf

#### Abrindo conexao 
con = arduino.abrir_conexao("COM3")

#### Funcao necessaria pra dar load no modelo
def contrastive_loss(y_true, y_pred):
    margin = 1
    return tf.math.reduce_mean(y_true * tf.math.square(y_pred) + (1 - y_true) * tf.math.square(tf.math.maximum(margin - y_pred, 0)))

#### Load no modelo
model = K.models.load_model("C:/Engenharia/Git/acionamento_mao_robo/model.h5", custom_objects={'contrastive_loss':contrastive_loss})

#### Checando conexao
if (con[1]):
    #### Abrindo camera
    cam = opencv.init_camera()
    #### Flag para desligar a camera
    flag_desliga_cam = False
    #### Captura de frame
    while(1):
        #### Captura
        frame = opencv.captura_frame(cam)
        #### Resize
        frame_resize = cv2.resize(frame, (160, 160))
        #### Mostra imagem
        cv2.imshow('image', frame_resize)
        if (cv2.waitKey(30) & 0xFF) == 27:
            flag_desliga_cam = True
            break
    #### Finaliza a conexao com a camera
    if (flag_desliga_cam):
        opencv.finalizar_camera(cam)
        arduino.fechar_conexao(con)