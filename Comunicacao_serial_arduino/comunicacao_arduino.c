#include <Servo.h>

#define Servo_1 
#define Servo_2 
#define Servo_3 
#define Servo_4   

Servo s1, s2, s3, s4 


void setup() 
{
    // Attach nos servos
    s1.attach(Servo_1)
    s2.attach(Servo_2)
    s3.attach(Servo_3)
    s4.attach(Servo_4)
    s5.attach(Servo_5)

    // Iniciando comunicação serial
    Serial.begin(9600);

}

void loop ()
{
    if(Serial.available() > 0)
    {
        // Caracter que vai receber os comandos vindos da serial
        char leitura = Serial.read();

        // Fazer divisao para que [0] == ":", [1] == "comando" e [2] == ":"
        

        // Acionar os motores
        switch (leitura)
        {
            case '1':
                Instruções;
            break;

            case '2':
                Instruções;
            break;

            default
                Instruções;
        }

    }
}

void atualizar_servo(int = comando)
{
    //PARA "pos" IGUAL A 0, ENQUANTO "pos" MENOR QUE 180, INCREMENTA "pos"
    for(pos = 0; pos < 180; pos++)
    { 
        s1.write(pos); //ESCREVE O VALOR DA POSIÇÃO QUE O SERVO DEVE GIRAR
        delay(15); //INTERVALO DE 15 MILISSEGUNDOS
    }
}