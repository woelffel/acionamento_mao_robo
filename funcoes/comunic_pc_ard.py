import serial

class arduino():

    def __init__(self):
        self.nada = 0
    #### Funcao para abrir conexao serial com a porta desejada
    def abrir_conexao(porta):
        #### Comecar comunicacao serial
        conexao = serial.Serial('/' + porta, 9600)

        #### Averiguando se conexao relamente esta aberta
        status_conexao = False
        if (conexao.isOpen()):
            status_conexao = True
        
        return (conexao, status_conexao)


    #### Funcao para enviar o comando
    def envia_comando(conexao, comando):
        '''
        Entradas:
            Conexao é o que retorna da funcao "abrir_conexao"
            Comando é um comando que vai de 1 a 5 que representa
                as classes de cada saída da rede
        Saída:
            Sem retorno
        '''
        #### Preparando mensagem
        mensagem = str(comando)
        conexao.write(mensagem.encode('utf-8'))
    
    #### Finaliza a conexao serial
    def fechar_conexao(conexao):
        conexao.close()


