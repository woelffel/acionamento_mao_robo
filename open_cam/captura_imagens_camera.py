import numpy as np
import cv2

### Inicializa a camera e retorna uma instancia da mesma
def inicializacao_camera():
    camera = cv2.VideoCapture(0)
    return camera

def captura_frame_gray():
    # Capture frame-by-frame
    ret, frame = camera.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    return gray

def show_image(frame, comando):
    ### Display the resulting frame
    ## Escrevendo o comando na tela
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10,500)
    fontScale              = 3
    fontColor              = (255,255,255)
    lineType               = 2

    cv2.putText(img, str(comando), 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        lineType)
    
    ## Mostrando a imagem com o texto
    cv2.imshow('frame',frame)
    '''
    Utilizar essa linha de código para quebrar o "while" que vai ter para
    capturar as imagens constantemente 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    '''

def finalizar_camera():
    # When everything done, release the capture
    camera.release()
    cv2.destroyAllWindows()