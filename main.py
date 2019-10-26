from funcoes.comunic_pc_ard import arduino
from funcoes.captura_img_cam import opencv
import cv2
from tensorflow import keras as K
import tensorflow as tf
import time

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
    #### Flag para predicao 
    flag_predicao == True
    #### Variaveis de tempo
    tempo1 = 0
    #### Captura de frame, predicao e mensagem
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
        #### Gera predicao caso flag verdadeira
        if (flag_predicao == True)
            comando = model.predict(frame_resize)
            flag_predicao = False
            #### Envia mensagem para arduino
            arduino.envia_comando(conexao = con[0], comando = (":" + str(comando) + ":"))
            #### Comeca a contagem de tempo esperando resposta do arduino
            tempo1 = time.time()
        if (time.time() - tempo1 > 10): ## Se tiver passado 30 segundos do envio do comando
            #### Espera mensagem de volta
            msg_back = arduino.recebe_mensagem(con[0])
            if (msg_back == "Mensagem_nao_valida"):
                print("Mensagem_nao_valida")
                flag_predicao = True
            elif(msg_back == "Comando_nao_valido"):
                print("Comando_nao_valido")
                flag_predicao = True
            elif (msg_back = "Ok"):
                flag_predicao = True
            else:
                print("Esperando_mensagem")
    #### Finaliza a conexao com a camera
    if (flag_desliga_cam):
        opencv.finalizar_camera(cam)
        arduino.fechar_conexao(con)