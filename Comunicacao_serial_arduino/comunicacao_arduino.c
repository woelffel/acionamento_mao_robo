/*#include <Servo.h>

#define Servo_1 
#define Servo_2 
#define Servo_3 
#define Servo_4   

Servo s1, s2, s3, s4 
*/

void setup() 
{
    /*/ Attach nos servos
    s1.attach(Servo_1)
    s2.attach(Servo_2)
    s3.attach(Servo_3)
    s4.attach(Servo_4)
    s5.attach(Servo_5)
    */
    // Iniciando comunicação serial
    Serial.begin(9600);
    
    // String que fica armazenada a mensagem
    String leitura;

    // Teste para acender led
    int led1 = 13;
    pinMode(led1, OUTPUT);
}
/*
void atualizar_servo(int = comando)
{
    //PARA "pos" IGUAL A 0, ENQUANTO "pos" MENOR QUE 180, INCREMENTA "pos"
    for(pos = 0; pos < 180; pos++)
    { 
        s1.write(pos); //ESCREVE O VALOR DA POSIÇÃO QUE O SERVO DEVE GIRAR
        delay(15); //INTERVALO DE 15 MILISSEGUNDOS
    }
}
*/
void reenviar_mensagem(const String& leitura)
{
    for (byte i = 0; i <= sizeof(leitura)-1; i++){
      Serial.write(leitura[i]);
    }
    Serial.flush();
}

void loop(){
    if(Serial.available() > 0)
    {
        // Caracter que vai receber os comandos vindos da serial
        leitura = Serial.readString();
        // Flag para mandar mensagens de volta
        char flag = '1';
        // Fazer divisao para que [0] == ":", [1] == "comando" e [2] == ":"
        if ((leitura[0] == ':') && (leitura[2] == ':')){
            // Acionar os motores
            switch (leitura[1])
            {
                case '1':
                    //Instruções;
                    digitalWrite(led1, HIGH);
                    // Chamar funcao para movimento servo comando 1
                    flag = '0';
                break;

                case '2':
                    //Instruções;
                    digitalWrite(led1, LOW);
                    // Chamar funcao para movimento servo comando 2
                    flag = '0';
                break;

                case '3':
                    //Instruções;
                    digitalWrite(led1, LOW);
                    // Chamar funcao para movimento servo comando 3
                    flag = '0';
                break;

                case '4':
                    //Instruções;
                    digitalWrite(led1, LOW);
                    // Chamar funcao para movimento servo comando 4
                    flag = '0';
                break;

                case '5':
                    //Instruções;
                    digitalWrite(led1, LOW);
                    // Chamar funcao para movimento servo comando 5
                    flag = '0';
                break;

                //default:
                    //Instruções;
            }
            if (flag == '0'){ // Se o comando dado e valido
                reenviar_mensagem(leitura);
            } else { // Se o comando dado nao e valido
              char erro1[] = ":9:";
              reenviar_mensagem(erro1);
            }
        } else { // Se a mensagem nao e valida
          char erro2[] = ":8:";
          reenviar_mensagem(erro2);
        }
    }
}